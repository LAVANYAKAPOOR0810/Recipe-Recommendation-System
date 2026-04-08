
from flask import redirect, url_for, session




from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# 🔐 Secret Key (used for session security)
app.secret_key = "secret123"

# 🗄️ Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ======================
# 📦 DATABASE MODELS
# ======================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Cookbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    recipe_name = db.Column(db.String(200))
    ingredients = db.Column(db.Text)


# ======================
# 📂 LOAD DATA + MODELS
# ======================

recipes_data = pd.read_csv("recipe_final1.csv")

model = pickle.load(open('recipe_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))


# ======================
# 🔐 AUTH ROUTES
# ======================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            return redirect('/')  # 🔥 FIXED
        else:
            return "Invalid credentials ❌"

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing = User.query.filter_by(username=username).first()
        if existing:
            return "User already exists!"

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')

    return render_template('register.html')


# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')


# ======================
# 🏠 HOME (RECOMMENDER)
# ======================

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return redirect('/login')

    recommendations = []

    if request.method == 'POST':
        try:
            calories = float(request.form['calories'])
            fat = float(request.form['fat'])
            carbs = float(request.form['carbohydrates'])
            protein = float(request.form['protein'])
            cholesterol = float(request.form['cholesterol'])
            sodium = float(request.form['sodium'])
            fiber = float(request.form['fiber'])
            ingredients = request.form['ingredients']

            # 🔹 Prepare input
            numeric_features = np.array([[calories, fat, carbs, protein, cholesterol, sodium, fiber]])
            numeric_scaled = scaler.transform(numeric_features)

            ingredients_vec = vectorizer.transform([ingredients]).toarray()

            final_input = np.hstack((numeric_scaled, ingredients_vec))

            # 🔹 Predict
            distances, indices = model.kneighbors(final_input)

            # 🔹 Get recipes
            for i in indices[0]:
                recipe = recipes_data.iloc[i]
                recommendations.append({
    "recipe_name": recipe['recipe_name'],
    "ingredients_list": recipe['ingredients_list'],
    "image_url": recipe.get('image_url', ''),
    "calories": recipe.get('calories', 0),
    "protein": recipe.get('protein', 0),
    "fat": recipe.get('fat', 0),
    "carbohydrates": recipe.get('carbohydrates', 0),
    "fiber": recipe.get('fiber', 0)
})

        except Exception as e:
            print("🔥 ERROR:", e)
            return f"Error occurred: {e}"

    return render_template('index.html', recommendations=recommendations)



# ======================
# ❤️ SAVE RECIPE
# ======================

from flask import jsonify

@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    if 'user_id' not in session:
        return jsonify({"message": "Login required ❌"})

    data = request.get_json()

    new_entry = Cookbook(
        user_id=session['user_id'],
        recipe_name=data['name'],
        ingredients=data['ingredients']
    )

    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Saved to Cookbook ❤️"})


# ======================
# 📖 VIEW COOKBOOK
# ======================

@app.route('/cookbook')
def cookbook():
    if 'user_id' not in session:
        return redirect('/login')

    user_recipes = Cookbook.query.filter_by(user_id=session['user_id']).all()

    return render_template('cookbook.html', recipes=user_recipes)

@app.route('/logout')
def logout():
    session.pop('user_id', None)   # remove logged-in user
    return redirect(url_for('login'))


# @app.route('/recipe/<name>')
# def recipe_detail(name):
#     recipe = recipes_data[recipes_data['recipe_name'] == name].iloc[0]

#     return render_template(
#         'recipe_detail.html',
#         recipe=recipe,
#         instructions=recipe.get('instructions', 'No instructions available')
#     )


@app.route('/recipe/<name>')
def recipe_detail(name):
    if 'user_id' not in session:
        return redirect('/login')

    recipe = recipes_data[recipes_data['recipe_name'] == name].iloc[0]

    ingredients = recipe['ingredients_list']

    # 🔥 SIMPLE AI INSTRUCTIONS (no API yet)
    instructions = f"""
    1. Prepare all ingredients: {ingredients}
    2. Heat a pan and add oil.
    3. Cook ingredients step by step.
    4. Add spices and mix well.
    5. Simmer until cooked properly.
    6. Serve hot and enjoy!
    """

    return render_template(
        'recipe_detail.html',
        recipe=recipe,
        instructions=instructions
    )

# from openai import OpenAI
# client = OpenAI()

def generate_instructions(name, ingredients):
    prompt = f"""
    Give step-by-step cooking instructions for:
    Recipe: {name}
    Ingredients: {ingredients}
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ======================
# 🚀 RUN APP
# ======================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # 🔥 creates DB if not exists

    app.run(debug=True)