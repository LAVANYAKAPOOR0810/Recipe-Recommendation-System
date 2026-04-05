# # from flask_sqlalchemy import SQLAlchemy
# # from flask import redirect, url_for, session



# # from flask import Flask, render_template, request
# # import numpy as np
# # import pandas as pd
# # from sklearn.neighbors import NearestNeighbors
# # from sklearn.preprocessing import StandardScaler
# # from sklearn.feature_extraction.text import TfidfVectorizer

# # app = Flask(__name__)

# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
# # app.config['SECRET_KEY'] = 'secret123'
# # db = SQLAlchemy(app)



# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(100), unique=True)
# #     password = db.Column(db.String(100))

# # class SavedRecipe(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     user_id = db.Column(db.Integer)
# #     name = db.Column(db.String(200))
# #     ingredients = db.Column(db.Text)
# #     image = db.Column(db.Text)

# #     with app.app_context():
# #         db.create_all()


# # # Absolute path example
# # data = pd.read_csv("recipe_final1.csv")

# # # Preprocess Ingredients
# # vectorizer = TfidfVectorizer()
# # X_ingredients = vectorizer.fit_transform(data['ingredients_list'])

# # # Normalize Numerical Features
# # scaler = StandardScaler()
# # X_numerical = scaler.fit_transform(data[['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']])

# # # Combine Features
# # X_combined = np.hstack([X_numerical, X_ingredients.toarray()])

# # # Train KNN Model
# # knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
# # knn.fit(X_combined)

# # def recommend_recipes(input_features):
# #     input_features_scaled = scaler.transform([input_features[:7]])
# #     input_ingredients_transformed = vectorizer.transform([input_features[7]])
# #     input_combined = np.hstack([input_features_scaled, input_ingredients_transformed.toarray()])
# #     distances, indices = knn.kneighbors(input_combined)
# #     recommendations = data.iloc[indices[0]]
# #     return recommendations[['recipe_name', 'ingredients_list', 'image_url',
# #                         'calories', 'fat', 'carbohydrates', 
# #                         'protein', 'fiber']].head(5)

# # # Function to truncate product name
# # def truncate(text, length):
# #     if len(text) > length:
# #         return text[:length] + "..."
# #     else:
# #         return text

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     if request.method == 'POST':
# #         calories = float(request.form['calories'])
# #         fat = float(request.form['fat'])
# #         carbohydrates = float(request.form['carbohydrates'])
# #         protein = float(request.form['protein'])
# #         cholesterol = float(request.form['cholesterol'])
# #         sodium = float(request.form['sodium'])
# #         fiber = float(request.form['fiber'])
# #         ingredients = request.form['ingredients']
# #         input_features = [calories, fat, carbohydrates, protein, cholesterol, sodium, fiber, ingredients]
# #         recommendations = recommend_recipes(input_features)
# #         return render_template('index.html', recommendations=recommendations.to_dict(orient='records'),truncate = truncate)
# #     return render_template('index.html', recommendations=[])

# # # @app.route('/cookbook')
# # # def cookbook():
# # #     return render_template('cookbook.html')




# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':

# #         username = request.form['username'].strip()
# #         password = request.form['password'].strip()

# #         user = User.query.filter_by(username=username).first()

# #         if user and user.password == password:
# #             session['user_id'] = user.id
# #             return redirect('/cookbook')   # 👈 IMPORTANT

# #         else:
# #             return "Invalid credentials ❌"

# #     return render_template('login.html')


# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     if request.method == 'POST':

# #         username = request.form['username'].strip()
# #         password = request.form['password'].strip()

# #         new_user = User(username=username, password=password)
# #         db.session.add(new_user)
# #         db.session.commit()

# #         return redirect('/login')

# #     return render_template('register.html') 



# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     return redirect('/')



# # @app.route('/save_recipe', methods=['POST'])
# # def save_recipe():
# #     if 'user_id' not in session:
# #         return {"message": "Login required"}

# #     data_json = request.get_json()

# #     new_recipe = SavedRecipe(
# #         user_id=session['user_id'],
# #         name=data_json['name'],
# #         ingredients=data_json['ingredients'],
# #         image=data_json['image']
# #     )

# #     db.session.add(new_recipe)
# #     db.session.commit()

# #     return {"message": "Saved to Cookbook ❤️"}


# # @app.route('/cookbook')
# # def cookbook():
# #     if 'user_id' not in session:
# #         return redirect('/login')

# #     recipes = SavedRecipe.query.filter_by(user_id=session['user_id']).all()
# #     return render_template('cookbook.html', recipes=recipes)



# # if __name__ == '__main__':
# #     app.run(debug=True)










# # # from flask import Flask, render_template, request
# # # import numpy as np
# # # import pandas as pd
# # # from sklearn.neighbors import NearestNeighbors
# # # from sklearn.preprocessing import StandardScaler
# # # from sklearn.feature_extraction.text import TfidfVectorizer
# # # import os

# # # app = Flask(__name__)

# # # # Load and preprocess data (only once)
# # # print("Loading dataset...")
# # # try:
# # #     data = pd.read_csv("recipe_final1.csv")
# # #     print(f"Dataset loaded: {len(data)} recipes")
# # # except FileNotFoundError:
# # #     print("ERROR: recipe_final1.csv not found!")
# # #     data = pd.DataFrame()

# # # if not data.empty:
# # #     # Preprocess Ingredients
# # #     print("Vectorizing ingredients...")
# # #     vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
# # #     X_ingredients = vectorizer.fit_transform(data['ingredients_list'].fillna(''))

# # #     # Normalize Numerical Features
# # #     print("Scaling numerical features...")
# # #     numerical_cols = ['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']
# # #     X_numerical = StandardScaler().fit_transform(data[numerical_cols].fillna(0))

# # #     # Combine Features
# # #     X_combined = np.hstack([X_numerical, X_ingredients.toarray()])

# # #     # Train KNN Model
# # #     print("Training KNN model...")
# # #     knn = NearestNeighbors(n_neighbors=6, metric='euclidean', algorithm='auto')
# # #     knn.fit(X_combined)
# # #     print("✅ Model ready!")
# # # else:
# # #     vectorizer = None
# # #     knn = None
# # #     print("⚠️ No data loaded - using dummy recommendations")

# # # def recommend_recipes(input_features):
# # #     if knn is None or data.empty:
# # #         # Dummy recommendations if no data
# # #         return pd.DataFrame([{
# # #             'recipe_name': 'Sample Recipe',
# # #             'ingredients_list': 'chicken, rice, vegetables',
# # #             'image_url': 'https://via.placeholder.com/400x220/4CAF50/FFFFFF?text=Recipe',
# # #             'calories': 350,
# # #             'fat': 12,
# # #             'carbohydrates': 45,
# # #             'protein': 25,
# # #             'fiber': 6
# # #         } for _ in range(3)])
    
# # #     try:
# # #         # Extract numerical and text features
# # #         num_features = input_features[:7]  # calories, fat, carbs, protein, cholesterol, sodium, fiber
# # #         ingredients_text = input_features[7]
        
# # #         # Scale numerical features
# # #         input_num_scaled = StandardScaler().fit_transform([num_features])
        
# # #         # Transform ingredients
# # #         input_ingredients = vectorizer.transform([ingredients_text])
        
# # #         # Combine
# # #         input_combined = np.hstack([input_num_scaled, input_ingredients.toarray()])
        
# # #         # Find nearest neighbors
# # #         distances, indices = knn.kneighbors(input_combined)
        
# # #         # Get recommendations with full nutrition info
# # #         recommendations = data.iloc[indices[0]].head(5).copy()
        
# # #         # Ensure all required columns exist
# # #         for col in ['calories', 'fat', 'carbohydrates', 'protein', 'fiber']:
# # #             if col not in recommendations.columns:
# # #                 recommendations[col] = 0
        
# # #         # Select and format output
# # #         result = recommendations[[
# # #             'recipe_name', 'ingredients_list', 'image_url', 
# # #             'calories', 'fat', 'carbohydrates', 'protein', 'fiber'
# # #         ]].fillna({
# # #             'image_url': 'https://via.placeholder.com/400x220/4CAF50/FFFFFF?text=No+Image',
# # #             'recipe_name': 'Unknown Recipe'
# # #         })
        
# # #         return result.to_dict(orient='records')
    
# # #     except Exception as e:
# # #         print(f"Recommendation error: {e}")
# # #         return []

# # # @app.route('/', methods=['GET', 'POST'])
# # # def index():
# # #     recommendations = []
# # #     show_results = False
    
# # #     if request.method == 'POST':
# # #         try:
# # #             # Get form data with defaults
# # #             form_data = {
# # #                 'calories': float(request.form.get('calories', 0)),
# # #                 'fat': float(request.form.get('fat', 0)),
# # #                 'carbohydrates': float(request.form.get('carbohydrates', 0)),
# # #                 'protein': float(request.form.get('protein', 0)),
# # #                 'cholesterol': float(request.form.get('cholesterol', 0)),
# # #                 'sodium': float(request.form.get('sodium', 0)),
# # #                 'fiber': float(request.form.get('fiber', 0)),
# # #                 'ingredients': request.form.get('ingredients', '').strip()
# # #             }
            
# # #             input_features = [
# # #                 form_data['calories'], form_data['fat'], form_data['carbohydrates'],
# # #                 form_data['protein'], form_data['cholesterol'], form_data['sodium'],
# # #                 form_data['fiber'], form_data['ingredients']
# # #             ]
            
# # #             recommendations = recommend_recipes(input_features)
# # #             show_results = True
            
# # #             print(f"✅ Found {len(recommendations)} recommendations")
            
# # #         except Exception as e:
# # #             print(f"❌ Form error: {e}")
# # #             show_results = True  # Show "no results" message
    
# # #     return render_template('index.html', 
# # #                          recommendations=recommendations, 
# # #                          show_results=show_results)

# # # if __name__ == '__main__':
# # #     app.run(debug=True, port=5000)








# import pandas as pd
# from flask import Flask, render_template, request, redirect, session, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# recipes_data = pd.read_csv("recipe_final1.csv")
# # 🔐 SECRET KEY (VERY IMPORTANT)
# app.secret_key = 'my_super_secret_key_123'

# # 🗄 DATABASE CONFIG
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # ===========================
# # 📦 DATABASE MODELS
# # ===========================

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))


# class SavedRecipe(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     name = db.Column(db.String(200))
#     ingredients = db.Column(db.Text)
#     image = db.Column(db.Text)


# # ===========================
# # 🛠 CREATE DATABASE
# # ===========================
# with app.app_context():
#     db.create_all()


# # ===========================
# # 🏠 HOME PAGE
# # ===========================
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if 'user_id' not in session:
#         return redirect('/login')

#     recommendations = None

#     if request.method == 'POST':
#         # 🔹 Get user input
#         calories = float(request.form['calories'])
#         fat = float(request.form['fat'])
#         carbs = float(request.form['carbohydrates'])
#         protein = float(request.form['protein'])
#         cholesterol = float(request.form['cholesterol'])
#         sodium = float(request.form['sodium'])
#         fiber = float(request.form['fiber'])
#         ingredients = request.form['ingredients']

#         # 🔥 LOAD MODEL FILES
#         import pickle
#         import numpy as np

#         model = pickle.load(open('recipe_model.pkl', 'rb'))
#         scaler = pickle.load(open('scaler.pkl', 'rb'))
#         vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
#         recipes_data = pickle.load(open('recipes.pkl', 'rb'))

#         # 🔹 Prepare input
#         numeric_features = np.array([[calories, fat, carbs, protein, cholesterol, sodium, fiber]])
#         numeric_scaled = scaler.transform(numeric_features)

#         ingredients_vec = vectorizer.transform([ingredients]).toarray()

#         final_input = np.hstack((numeric_scaled, ingredients_vec))

#         # 🔹 Predict
#         distances, indices = model.kneighbors(final_input)

#         # 🔹 Get recommendations
#         recommendations = []
#         for i in indices[0]:
#             recipe = recipes_data.iloc[i]
#             recommendations.append({
#                 "recipe_name": recipe['recipe_name'],
#                 "ingredients_list": recipe['ingredients_list'],
#                 "image_url": recipe.get('image_url', ''),
#                 "calories": recipe.get('calories', 0),
#                 "protein": recipe.get('protein', 0),
#                 "fat": recipe.get('fat', 0),
#                 "carbohydrates": recipe.get('carbohydrates', 0),
#                 "fiber": recipe.get('fiber', 0)
#             })

#     return render_template('index.html', recommendations=recommendations)


# # ===========================
# # 🔐 REGISTER
# # ===========================
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username'].strip()
#         password = request.form['password'].strip()

#         existing = User.query.filter_by(username=username).first()
#         if existing:
#             return "User already exists ❌"

#         new_user = User(username=username, password=password)
#         db.session.add(new_user)
#         db.session.commit()

#         return redirect('/login')

#     return render_template('register.html')


# # ===========================
# # 🔐 LOGIN
# # ===========================
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username'].strip()
#         password = request.form['password'].strip()

#         user = User.query.filter_by(username=username).first()

#         if user and user.password == password:
#             session['user_id'] = user.id  # ✅ SESSION STORED
#             return redirect('/cookbook')  # ✅ GO TO COOKBOOK

#         else:
#             return "Invalid credentials ❌"

#     return render_template('login.html')


# # ===========================
# # ❤️ SAVE RECIPE
# # ===========================
# @app.route('/save_recipe', methods=['POST'])
# def save_recipe():
#     if 'user_id' not in session:
#         return jsonify({"message": "Please login first ❌"})

#     data = request.get_json()

#     recipe = SavedRecipe(
#         user_id=session['user_id'],
#         name=data['name'],
#         ingredients=data['ingredients'],
#         image=data['image']
#     )

#     db.session.add(recipe)
#     db.session.commit()

#     return jsonify({"message": "Saved to Cookbook ❤️"})


# # ===========================
# # 📖 COOKBOOK PAGE
# # ===========================
# @app.route('/cookbook')
# def cookbook():
#     if 'user_id' not in session:
#         return redirect('/login')

#     recipes = SavedRecipe.query.filter_by(user_id=session['user_id']).all()

#     return render_template('cookbook.html', recipes=recipes)


# # ===========================
# # 🚪 LOGOUT
# # ===========================
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')


# # ===========================
# # ▶ RUN APP
# # ===========================
# if __name__ == '__main__':
#     app.run(debug=True)






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



# ======================
# 🚀 RUN APP
# ======================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # 🔥 creates DB if not exists

    app.run(debug=True)