# # # from flask import Flask, render_template, request, redirect, session, url_for, jsonify
# # # from flask_sqlalchemy import SQLAlchemy
# # # import pandas as pd
# # # import numpy as np
# # # import os
# # # import warnings
# # # warnings.filterwarnings('ignore')

# # # app = Flask(__name__, static_folder='static')
# # # app.secret_key = os.urandom(24)
# # # app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # # db = SQLAlchemy(app)

# # # # ======================
# # # # DATABASE MODELS
# # # # ======================
# # # class User(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     username = db.Column(db.String(100), unique=True)
# # #     password = db.Column(db.String(100))

# # # class Cookbook(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     user_id = db.Column(db.Integer)
# # #     recipe_name = db.Column(db.String(200))
# # #     ingredients = db.Column(db.Text)
# # #     image = db.Column(db.String(500))

# # # # ======================
# # # # 🥗 5 DEMO RECIPES
# # # # ======================
# # # DEMO_RECIPES = [
# # #     {
# # #         "recipe_name": "Chicken Rice Bowl 🇨🇳",
# # #         "ingredients_list": "chicken breast, jasmine rice, broccoli, soy sauce, garlic, ginger",
# # #         "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400",
# # #         "cuisine": "asian",
# # #         "calories": 450,
# # #         "protein": 35.0,
# # #         "carbohydrates": 50.0,
# # #         "fat": 12.0
# # #     },
# # #     {
# # #         "recipe_name": "Veggie Stir Fry 🥦",
# # #         "ingredients_list": "tofu, bell peppers, broccoli, carrots, teriyaki sauce, sesame oil",
# # #         "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400", 
# # #         "cuisine": "asian",
# # #         "calories": 320,
# # #         "protein": 18.0,
# # #         "carbohydrates": 45.0,
# # #         "fat": 8.0
# # #     },
# # #     {
# # #         "recipe_name": "Grilled Salmon Salad 🐟",
# # #         "ingredients_list": "salmon fillet, mixed greens, cherry tomatoes, olive oil, lemon juice",
# # #         "image_url": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400",
# # #         "cuisine": "mediterranean", 
# # #         "calories": 380,
# # #         "protein": 28.0,
# # #         "carbohydrates": 15.0,
# # #         "fat": 22.0
# # #     },
# # #     {
# # #         "recipe_name": "Quinoa Chickpea Bowl 🌾",
# # #         "ingredients_list": "quinoa, chickpeas, avocado, cucumber, tahini dressing, lemon",
# # #         "image_url": "https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?w=400",
# # #         "cuisine": "mediterranean",
# # #         "calories": 420,
# # #         "protein": 15.0,
# # #         "carbohydrates": 55.0,
# # #         "fat": 18.0
# # #     },
# # #     {
# # #         "recipe_name": "Thai Tofu Curry 🌶️",
# # #         "ingredients_list": "tofu, coconut milk, red curry paste, bamboo shoots, rice noodles",
# # #         "image_url": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400",
# # #         "cuisine": "thai",
# # #         "calories": 480,
# # #         "protein": 20.0,
# # #         "carbohydrates": 60.0,
# # #         "fat": 25.0
# # #     }
# # # ]

# # # recipes_data = pd.DataFrame(DEMO_RECIPES)

# # # # ======================
# # # # 🔐 AUTH ROUTES
# # # # ======================
# # # @app.route('/login', methods=['GET', 'POST'])
# # # def login():
# # #     if request.method == 'POST':
# # #         username = request.form['username']
# # #         password = request.form['password']
# # #         user = User.query.filter_by(username=username, password=password).first()
# # #         if user:
# # #             session['user_id'] = user.id
# # #             return redirect('/')
# # #         return render_template('login.html', error="❌ Invalid credentials!")
# # #     session.clear()
# # #     return render_template('login.html')

# # # @app.route('/register', methods=['GET', 'POST'])
# # # def register():
# # #     if request.method == 'POST':
# # #         username = request.form['username']
# # #         password = request.form['password']
# # #         if not User.query.filter_by(username=username).first():
# # #             user = User(username=username, password=password)
# # #             db.session.add(user)
# # #             db.session.commit()
# # #             return redirect('/login')
# # #         return render_template('register.html', error="❌ User exists!")
# # #     return render_template('register.html')

# # # @app.route('/logout')
# # # def logout():
# # #     session.clear()
# # #     return redirect('/login')

# # # # ======================
# # # # 🏠 HOME - 3 RECIPES GUARANTEED!
# # # # ======================
# # # @app.route('/', methods=['GET', 'POST'])
# # # def home():
# # #     if 'user_id' not in session:
# # #         return redirect('/login')

# # #     recommendations = []
# # #     form_data = {}

# # #     if request.method == 'POST':
# # #         ingredients = request.form.get('ingredients', '').lower().strip()
# # #         cuisine = request.form.get('cuisine', '').lower().strip()
# # #         calories = float(request.form.get('calories', 400))

# # #         print(f"🔍 ingredients='{ingredients}', cuisine='{cuisine}', cal={calories}")

# # #         # Find matches
# # #         matches = []
# # #         for idx, recipe in recipes_data.iterrows():
# # #             score = 0
# # #             r_name = str(recipe['recipe_name']).lower()
# # #             r_ing = str(recipe['ingredients_list']).lower()
# # #             r_cui = str(recipe['cuisine']).lower()
            
# # #             # Ingredient match
# # #             for word in ingredients.split(','):
# # #                 word = word.strip()
# # #                 if word and (word in r_ing or word in r_name):
# # #                     score += 40
            
# # #             # Cuisine match
# # #             if cuisine in r_cui or not cuisine:
# # #                 score += 30
            
# # #             # Calorie match
# # #             if abs(recipe['calories'] - calories) < 150:
# # #                 score += 20
            
# # #             if score > 10:
# # #                 matches.append({'idx': idx, 'score': score})

# # #         # Sort and get TOP 3
# # #         matches.sort(key=lambda x: x['score'], reverse=True)
# # #         top_indices = [m['idx'] for m in matches[:3]]

# # #         # If less than 3, fill with best recipes
# # #         while len(top_indices) < 3:
# # #             top_indices.append(len(top_indices) % len(recipes_data))

# # #         # Create recommendations
# # #         for idx in top_indices:
# # #             recipe = recipes_data.iloc[idx]
# # #             recommendations.append({
# # #                 'recipe_name': recipe['recipe_name'],
# # #                 'ingredients_list': recipe['ingredients_list'],
# # #                 'image_url': recipe['image_url'],
# # #                 'cuisine': recipe['cuisine'],
# # #                 'calories': int(recipe['calories']),
# # #                 'protein': float(recipe['protein']),
# # #                 'carbohydrates': float(recipe['carbohydrates']),
# # #                 'fat': float(recipe['fat'])
# # #             })

# # #         # Tiny session
# # #         session['rec_ids'] = top_indices
# # #         session['form_data'] = {k: str(v)[:30] for k, v in request.form.items()}

# # #     else:
# # #         # Load from session
# # #         rec_ids = session.get('rec_ids', [0,1,2])
# # #         for idx in rec_ids[:3]:
# # #             if idx < len(recipes_data):
# # #                 recipe = recipes_data.iloc[idx]
# # #                 recommendations.append({
# # #                     'recipe_name': recipe['recipe_name'],
# # #                     'ingredients_list': recipe['ingredients_list'],
# # #                     'image_url': recipe['image_url'],
# # #                     'cuisine': recipe['cuisine'],
# # #                     'calories': int(recipe['calories']),
# # #                     'protein': float(recipe['protein']),
# # #                     'carbohydrates': float(recipe['carbohydrates']),
# # #                     'fat': float(recipe['fat'])
# # #                 })

# # #     form_data = session.get('form_data', {})
# # #     return render_template('index.html', recommendations=recommendations, form_data=form_data)

# # # # ======================
# # # # ❤️ SAVE RECIPE
# # # # ======================
# # # @app.route('/save_recipe', methods=['POST'])
# # # def save_recipe():
# # #     if 'user_id' not in session:
# # #         return jsonify({'message': 'Login required ❌'})

# # #     data = request.get_json()
# # #     name = data.get('name', '')[:150]

# # #     # Check duplicate
# # #     existing = Cookbook.query.filter_by(user_id=session['user_id'], recipe_name=name).first()
# # #     if existing:
# # #         return jsonify({'message': 'Already saved ⚠️'})

# # #     recipe = Cookbook(
# # #         user_id=session['user_id'],
# # #         recipe_name=name,
# # #         ingredients=data.get('ingredients', '')[:500],
# # #         image=data.get('image', '')[:200]
# # #     )
# # #     db.session.add(recipe)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Saved to Cookbook ❤️'})

# # # # ======================
# # # # 📚 COOKBOOK
# # # # ======================
# # # @app.route('/cookbook')
# # # def cookbook():
# # #     if 'user_id' not in session:
# # #         return redirect('/login')
# # #     recipes = Cookbook.query.filter_by(user_id=session['user_id']).all()
# # #     return render_template('cookbook.html', recipes=recipes)

# # # # ======================
# # # # 🍳 RECIPE DETAIL - FIXED!
# # # # ======================
# # # @app.route('/recipe/<path:name>')
# # # def recipe_detail(name):
# # #     if 'user_id' not in session:
# # #         return redirect('/login')
    
# # #     name = unquote(name)
    
# # #     # Find recipe by name
# # #     for _, recipe in recipes_data.iterrows():
# # #         if recipe['recipe_name'] == name:
# # #             instructions = """
# # #             <ol class="list-group list-group-numbered">
# # #                 <li class="list-group-item">Gather all ingredients</li>
# # #                 <li class="list-group-item">Heat oil in pan (medium heat)</li>
# # #                 <li class="list-group-item">Cook main protein 5-7 mins</li>
# # #                 <li class="list-group-item">Add veggies & spices</li>
# # #                 <li class="list-group-item">Simmer 10 mins until done</li>
# # #                 <li class="list-group-item">Serve hot! 🌟</li>
# # #             </ol>
# # #             """
# # #             return render_template('recipe_detail.html', recipe=recipe.to_dict(), instructions=instructions)
    
# # #     return "Recipe not found ❌", 404

# # # # ======================
# # # # 🗑 DELETE - FIXED!
# # # # ======================
# # # @app.route('/delete_recipe/<int:id>', methods=['POST'])
# # # def delete_recipe(id):
# # #     if 'user_id' not in session:
# # #         return jsonify({'message': 'Login required ❌'}), 401
    
# # #     recipe = Cookbook.query.get(id)
# # #     if recipe and recipe.user_id == session['user_id']:
# # #         db.session.delete(recipe)
# # #         db.session.commit()
# # #         return jsonify({'message': 'Removed from Cookbook 🗑️'})
    
# # #     return jsonify({'message': 'Not found ❌'}), 404

# # # # ======================
# # # # 🔄 CLEAR
# # # # ======================
# # # @app.route('/clear_search')
# # # def clear_search():
# # #     session.pop('rec_ids', None)
# # #     session.pop('form_data', None)
# # #     return redirect('/')

# # # # ======================
# # # # START
# # # # ======================
# # # if __name__ == '__main__':
# # #     with app.app_context():
# # #         db.create_all()
# # #     print("🚀 http://127.0.0.1:5001")
# # #     app.run(debug=True, port=5001, host='127.0.0.1')




# # from flask import Flask, render_template, request, redirect, session, url_for, jsonify
# # from flask_sqlalchemy import SQLAlchemy
# # from urllib.parse import unquote  # ✅ FIXED - ADD THIS!
# # import pandas as pd
# # import numpy as np
# # import os
# # import warnings
# # warnings.filterwarnings('ignore')

# # app = Flask(__name__, static_folder='static')
# # app.secret_key = os.urandom(24)
# # app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)

# # # [REST OF YOUR CODE REMAINS SAME - JUST ADD the unquote import above]

# # # ======================
# # # DATABASE MODELS
# # # ======================
# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(100), unique=True)
# #     password = db.Column(db.String(100))

# # class Cookbook(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     user_id = db.Column(db.Integer)
# #     recipe_name = db.Column(db.String(200))
# #     ingredients = db.Column(db.Text)
# #     image = db.Column(db.String(500))

# # # ======================
# # # 🥗 5 DEMO RECIPES
# # # ======================
# # DEMO_RECIPES = [
# #     {
# #         "recipe_name": "Chicken Rice Bowl 🇨🇳",
# #         "ingredients_list": "chicken breast, jasmine rice, broccoli, soy sauce, garlic, ginger",
# #         "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400",
# #         "cuisine": "asian",
# #         "calories": 450,
# #         "protein": 35.0,
# #         "carbohydrates": 50.0,
# #         "fat": 12.0
# #     },
# #     {
# #         "recipe_name": "Veggie Stir Fry 🥦",
# #         "ingredients_list": "tofu, bell peppers, broccoli, carrots, teriyaki sauce, sesame oil",
# #         "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400", 
# #         "cuisine": "asian",
# #         "calories": 320,
# #         "protein": 18.0,
# #         "carbohydrates": 45.0,
# #         "fat": 8.0
# #     },
# #     {
# #         "recipe_name": "Grilled Salmon Salad 🐟",
# #         "ingredients_list": "salmon fillet, mixed greens, cherry tomatoes, olive oil, lemon juice",
# #         "image_url": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400",
# #         "cuisine": "mediterranean", 
# #         "calories": 380,
# #         "protein": 28.0,
# #         "carbohydrates": 15.0,
# #         "fat": 22.0
# #     },
# #     {
# #         "recipe_name": "Quinoa Chickpea Bowl 🌾",
# #         "ingredients_list": "quinoa, chickpeas, avocado, cucumber, tahini dressing, lemon",
# #         "image_url": "https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?w=400",
# #         "cuisine": "mediterranean",
# #         "calories": 420,
# #         "protein": 15.0,
# #         "carbohydrates": 55.0,
# #         "fat": 18.0
# #     },
# #     {
# #         "recipe_name": "Thai Tofu Curry 🌶️",
# #         "ingredients_list": "tofu, coconut milk, red curry paste, bamboo shoots, rice noodles",
# #         "image_url": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400",
# #         "cuisine": "thai",
# #         "calories": 480,
# #         "protein": 20.0,
# #         "carbohydrates": 60.0,
# #         "fat": 25.0
# #     }
# # ]

# # recipes_data = pd.DataFrame(DEMO_RECIPES)

# # # ======================
# # # 🔐 AUTH ROUTES
# # # ======================
# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         user = User.query.filter_by(username=username, password=password).first()
# #         if user:
# #             session['user_id'] = user.id
# #             return redirect('/')
# #         return render_template('login.html', error="❌ Invalid credentials!")
# #     session.clear()
# #     return render_template('login.html')

# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         password = request.form['password']
# #         if not User.query.filter_by(username=username).first():
# #             user = User(username=username, password=password)
# #             db.session.add(user)
# #             db.session.commit()
# #             return redirect('/login')
# #         return render_template('register.html', error="❌ User exists!")
# #     return render_template('register.html')

# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     return redirect('/login')

# # # ======================
# # # 🏠 HOME - 3 RECIPES GUARANTEED!
# # # ======================
# # @app.route('/', methods=['GET', 'POST'])
# # def home():
# #     if 'user_id' not in session:
# #         return redirect('/login')

# #     recommendations = []
# #     form_data = {}

# #     if request.method == 'POST':
# #         ingredients = request.form.get('ingredients', '').lower().strip()
# #         cuisine = request.form.get('cuisine', '').lower().strip()
# #         calories = float(request.form.get('calories', 400))

# #         print(f"🔍 ingredients='{ingredients}', cuisine='{cuisine}', cal={calories}")

# #         # Find matches
# #         matches = []
# #         for idx, recipe in recipes_data.iterrows():
# #             score = 0
# #             r_name = str(recipe['recipe_name']).lower()
# #             r_ing = str(recipe['ingredients_list']).lower()
# #             r_cui = str(recipe['cuisine']).lower()
            
# #             # Ingredient match
# #             for word in ingredients.split(','):
# #                 word = word.strip()
# #                 if word and (word in r_ing or word in r_name):
# #                     score += 40
            
# #             # Cuisine match
# #             if cuisine in r_cui or not cuisine:
# #                 score += 30
            
# #             # Calorie match
# #             if abs(recipe['calories'] - calories) < 150:
# #                 score += 20
            
# #             if score > 10:
# #                 matches.append({'idx': idx, 'score': score})

# #         # Sort and get TOP 3
# #         matches.sort(key=lambda x: x['score'], reverse=True)
# #         top_indices = [m['idx'] for m in matches[:3]]

# #         # Always ensure 3 recipes
# #         while len(top_indices) < 3:
# #             top_indices.append(len(top_indices) % len(recipes_data))

# #         # Create recommendations
# #         for idx in top_indices:
# #             recipe = recipes_data.iloc[idx]
# #             recommendations.append({
# #                 'recipe_name': recipe['recipe_name'],
# #                 'ingredients_list': recipe['ingredients_list'],
# #                 'image_url': recipe['image_url'],
# #                 'cuisine': recipe['cuisine'],
# #                 'calories': int(recipe['calories']),
# #                 'protein': float(recipe['protein']),
# #                 'carbohydrates': float(recipe['carbohydrates']),
# #                 'fat': float(recipe['fat'])
# #             })

# #         # Tiny session
# #         session['rec_ids'] = top_indices
# #         session['form_data'] = {k: str(v)[:30] for k, v in request.form.items()}

# #     else:
# #         # Load from session or default
# #         rec_ids = session.get('rec_ids', [0,1,2])
# #         for idx in rec_ids[:3]:
# #             if idx < len(recipes_data):
# #                 recipe = recipes_data.iloc[idx]
# #                 recommendations.append({
# #                     'recipe_name': recipe['recipe_name'],
# #                     'ingredients_list': recipe['ingredients_list'],
# #                     'image_url': recipe['image_url'],
# #                     'cuisine': recipe['cuisine'],
# #                     'calories': int(recipe['calories']),
# #                     'protein': float(recipe['protein']),
# #                     'carbohydrates': float(recipe['carbohydrates']),
# #                     'fat': float(recipe['fat'])
# #                 })

# #     form_data = session.get('form_data', {})
# #     return render_template('index.html', recommendations=recommendations, form_data=form_data)

# # # ======================
# # # ❤️ SAVE RECIPE
# # # ======================
# # @app.route('/save_recipe', methods=['POST'])
# # def save_recipe():
# #     if 'user_id' not in session:
# #         return jsonify({'message': 'Login required ❌'})

# #     data = request.get_json()
# #     name = data.get('name', '')[:150]

# #     # Check duplicate
# #     existing = Cookbook.query.filter_by(user_id=session['user_id'], recipe_name=name).first()
# #     if existing:
# #         return jsonify({'message': 'Already saved ⚠️'})

# #     recipe = Cookbook(
# #         user_id=session['user_id'],
# #         recipe_name=name,
# #         ingredients=data.get('ingredients', '')[:500],
# #         image=data.get('image', '')[:200]
# #     )
# #     db.session.add(recipe)
# #     db.session.commit()
# #     return jsonify({'message': 'Saved to Cookbook ❤️'})

# # # ======================
# # # 📚 COOKBOOK
# # # ======================
# # @app.route('/cookbook')
# # def cookbook():
# #     if 'user_id' not in session:
# #         return redirect('/login')
# #     recipes = Cookbook.query.filter_by(user_id=session['user_id']).all()
# #     return render_template('cookbook.html', recipes=recipes)

# # # ======================
# # # 🍳 RECIPE DETAIL - NOW WORKS!
# # # ======================
# # @app.route('/recipe/<path:name>')
# # def recipe_detail(name):
# #     if 'user_id' not in session:
# #         return redirect('/login')
    
# #     name = unquote(name)  # ✅ NOW WORKS!
    
# #     # Find exact recipe match
# #     for _, recipe in recipes_data.iterrows():
# #         if recipe['recipe_name'] == name:
# #             instructions = """
# #             <div class="mt-3">
# #                 <h5>🍳 Step-by-Step Instructions:</h5>
# #                 <ol>
# #                     <li>Prepare all your ingredients</li>
# #                     <li>Heat 1-2 tbsp oil in a pan</li>
# #                     <li>Cook protein/veggies 5-7 minutes</li>
# #                     <li>Add sauces/spices to taste</li>
# #                     <li>Simmer covered for 10 minutes</li>
# #                     <li>Serve hot and enjoy! 🌟</li>
# #                 </ol>
# #             </div>
# #             """
# #             return render_template('recipe_detail.html', 
# #                                  recipe={
# #                                     'recipe_name': recipe['recipe_name'],
# #                                     'ingredients_list': recipe['ingredients_list'],
# #                                     'image_url': recipe['image_url'],
# #                                     'cuisine': recipe['cuisine'],
# #                                     'calories': int(recipe['calories']),
# #                                     'protein': float(recipe['protein'])
# #                                  }, 
# #                                  instructions=instructions)
    
# #     return "Recipe not found ❌", 404

# # # ======================
# # # 🗑 DELETE - FIXED!
# # # ======================
# # @app.route('/delete_recipe/<int:id>', methods=['POST'])
# # def delete_recipe(id):
# #     if 'user_id' not in session:
# #         return jsonify({'message': 'Login required ❌'}), 401
    
# #     recipe = Cookbook.query.get(id)
# #     if recipe and recipe.user_id == session['user_id']:
# #         db.session.delete(recipe)
# #         db.session.commit()
# #         return jsonify({'message': 'Removed from Cookbook 🗑️'})
    
# #     return jsonify({'message': 'Not found ❌'}), 404

# # # ======================
# # # 🔄 CLEAR
# # # ======================
# # @app.route('/clear_search')
# # def clear_search():
# #     session.pop('rec_ids', None)
# #     session.pop('form_data', None)
# #     return redirect('/')

# # if __name__ == '__main__':
# #     with app.app_context():
# #         db.create_all()
# #     print("🚀 http://127.0.0.1:5001 - ALL FIXED!")
# #     app.run(debug=True, port=5001, host='127.0.0.1')





# from flask import Flask, render_template, request, redirect, session, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from urllib.parse import unquote
# import pandas as pd
# import numpy as np
# import os
# import warnings
# warnings.filterwarnings('ignore')

# app = Flask(__name__, static_folder='static')
# app.secret_key = os.urandom(24)
# app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # ======================
# # DATABASE MODELS (unchanged)
# # ======================
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))

# class Cookbook(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     recipe_name = db.Column(db.String(200))
#     ingredients = db.Column(db.Text)
#     image = db.Column(db.String(500))

# # ======================
# # 🥗 DEMO RECIPES (unchanged)
# # ======================
# DEMO_RECIPES = [
#     {
#         "recipe_name": "Chicken Rice Bowl 🇨🇳",
#         "ingredients_list": "chicken breast, jasmine rice, broccoli, soy sauce, garlic, ginger",
#         "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400",
#         "cuisine": "asian",
#         "calories": 450,
#         "protein": 35.0,
#         "carbohydrates": 50.0,
#         "fat": 12.0
#     },
#     {
#         "recipe_name": "Veggie Stir Fry 🥦",
#         "ingredients_list": "tofu, bell peppers, broccoli, carrots, teriyaki sauce, sesame oil",
#         "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400", 
#         "cuisine": "asian",
#         "calories": 320,
#         "protein": 18.0,
#         "carbohydrates": 45.0,
#         "fat": 8.0
#     },
#     {
#         "recipe_name": "Grilled Salmon Salad 🐟",
#         "ingredients_list": "salmon fillet, mixed greens, cherry tomatoes, olive oil, lemon juice",
#         "image_url": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400",
#         "cuisine": "mediterranean", 
#         "calories": 380,
#         "protein": 28.0,
#         "carbohydrates": 15.0,
#         "fat": 22.0
#     },
#     {
#         "recipe_name": "Quinoa Chickpea Bowl 🌾",
#         "ingredients_list": "quinoa, chickpeas, avocado, cucumber, tahini dressing, lemon",
#         "image_url": "https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?w=400",
#         "cuisine": "mediterranean",
#         "calories": 420,
#         "protein": 15.0,
#         "carbohydrates": 55.0,
#         "fat": 18.0
#     },
#     {
#         "recipe_name": "Thai Tofu Curry 🌶️",
#         "ingredients_list": "tofu, coconut milk, red curry paste, bamboo shoots, rice noodles",
#         "image_url": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400",
#         "cuisine": "thai",
#         "calories": 480,
#         "protein": 20.0,
#         "carbohydrates": 60.0,
#         "fat": 25.0
#     }
# ]

# recipes_data = pd.DataFrame(DEMO_RECIPES)

# # ======================
# # 🔐 AUTH ROUTES (unchanged)
# # ======================
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username, password=password).first()
#         if user:
#             session['user_id'] = user.id
#             return redirect('/')
#         return render_template('login.html', error="❌ Invalid credentials!")
#     session.clear()
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if not User.query.filter_by(username=username).first():
#             user = User(username=username, password=password)
#             db.session.add(user)
#             db.session.commit()
#             return redirect('/login')
#         return render_template('register.html', error="❌ User exists!")
#     return render_template('register.html')

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login')

# # ======================
# # 🏠 HOME - FRESH EVERY TIME! ✅
# # ======================
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if 'user_id' not in session:
#         return redirect('/login')

#     recommendations = []
#     form_data = {}

#     # ✅ ALWAYS FRESH ON GET (No old recommendations)
#     if request.method == 'GET':
#         # Clear old recommendations on fresh load
#         session.pop('recommendations', None)
#         session.pop('form_data', None)
#         session.pop('rec_ids', None)
#         return render_template('index.html', recommendations=[], form_data={})

#     # ✅ ONLY ON POST - Generate NEW recommendations
#     if request.method == 'POST':
#         print("🔥 NEW SEARCH!")
        
#         # Get ALL form data
#         ingredients = request.form.get('ingredients', '').lower().strip()
#         cuisine = request.form.get('cuisine', '').lower().strip()
#         calories = float(request.form.get('calories', 400))
#         protein = float(request.form.get('protein', 20))
#         fat = float(request.form.get('fat', 15))
#         carbs = float(request.form.get('carbohydrates', 50))

#         print(f"📊 Search: {ingredients} | {cuisine} | {calories}cal | {protein}g protein")

#         # Calculate match scores
#         matches = []
#         for idx, recipe in recipes_data.iterrows():
#             score = 0
            
#             # Ingredient matching
#             r_ing = str(recipe['ingredients_list']).lower()
#             r_name = str(recipe['recipe_name']).lower()
#             for word in ingredients.split(','):
#                 word = word.strip()
#                 if word and (word in r_ing or word in r_name):
#                     score += 30
            
#             # Cuisine matching
#             r_cui = str(recipe['cuisine']).lower()
#             if cuisine in r_cui or not cuisine:
#                 score += 25
            
#             # Nutrition matching
#             if abs(recipe['calories'] - calories) < 100:
#                 score += 20
#             if abs(recipe['protein'] - protein) < 10:
#                 score += 15
#             if abs(recipe['fat'] - fat) < 8:
#                 score += 10
#             if abs(recipe['carbohydrates'] - carbs) < 20:
#                 score += 10

#             matches.append({'idx': idx, 'score': score})

#         # Sort by score and get TOP 3
#         matches.sort(key=lambda x: x['score'], reverse=True)
#         top_indices = [m['idx'] for m in matches[:3]]

#         print(f"📈 Top indices: {top_indices}")

#         # Build recommendations
#         for idx in top_indices:
#             recipe = recipes_data.iloc[idx]
#             recommendations.append({
#                 'recipe_name': recipe['recipe_name'],
#                 'ingredients_list': recipe['ingredients_list'],
#                 'image_url': recipe['image_url'],
#                 'cuisine': recipe['cuisine'],
#                 'calories': int(recipe['calories']),
#                 'protein': float(recipe['protein']),
#                 'carbohydrates': float(recipe['carbohydrates']),
#                 'fat': float(recipe['fat'])
#             })

#         # ✅ NEW: Store ONLY search hash (not full data)
#         search_hash = f"{ingredients}_{cuisine}_{calories}"
#         session['search_hash'] = search_hash
#         session['form_data'] = {k: str(v)[:30] for k, v in request.form.items()}

#         print(f"✅ Generated {len(recommendations)} fresh recommendations!")

#     form_data = session.get('form_data', {})
#     return render_template('index.html', recommendations=recommendations, form_data=form_data)

# # ======================
# # ADD / CLEAR BUTTONS
# # ======================
# @app.route('/clear_search')
# def clear_search():
#     session.pop('search_hash', None)
#     session.pop('form_data', None)
#     return redirect('/')

# # ======================
# # OTHER ROUTES (unchanged)
# # ======================
# @app.route('/save_recipe', methods=['POST'])
# def save_recipe():
#     if 'user_id' not in session:
#         return jsonify({'message': 'Login required ❌'})
#     data = request.get_json()
#     name = data.get('name', '')[:150]
#     if not Cookbook.query.filter_by(user_id=session['user_id'], recipe_name=name).first():
#         recipe = Cookbook(user_id=session['user_id'], recipe_name=name,
#                          ingredients=data.get('ingredients', '')[:500],
#                          image=data.get('image', '')[:200])
#         db.session.add(recipe)
#         db.session.commit()
#     return jsonify({'message': 'Saved ❤️'})

# @app.route('/cookbook')
# def cookbook():
#     if 'user_id' not in session: return redirect('/login')
#     recipes = Cookbook.query.filter_by(user_id=session['user_id']).all()
#     return render_template('cookbook.html', recipes=recipes)

# @app.route('/recipe/<path:name>')
# def recipe_detail(name):
#     if 'user_id' not in session: return redirect('/login')
#     name = unquote(name)
#     for _, recipe in recipes_data.iterrows():
#         if recipe['recipe_name'] == name:
#             instructions = """
#             <div class="mt-3">
#                 <h5>🍳 Cooking Steps:</h5>
#                 <ol>
#                     <li>Gather ingredients</li>
#                     <li>Heat oil in pan</li>
#                     <li>Cook 5-7 mins</li>
#                     <li>Add spices</li>
#                     <li>Simmer 10 mins</li>
#                     <li>Serve hot! 🌟</li>
#                 </ol>
#             </div>
#             """
#             return render_template('recipe_detail.html', 
#                                  recipe=recipe.to_dict(), 
#                                  instructions=instructions)
#     return "Not found", 404

# @app.route('/delete_recipe/<int:id>', methods=['POST'])
# def delete_recipe(id):
#     if 'user_id' not in session: return jsonify({'message': 'Login!'})
#     recipe = Cookbook.query.get(id)
#     if recipe and recipe.user_id == session['user_id']:
#         db.session.delete(recipe)
#         db.session.commit()
#         return jsonify({'message': 'Removed 🗑️'})
#     return jsonify({'message': 'Not found'})

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     print("🚀 FRESH RECOMMENDATIONS! http://127.0.0.1:5001")
#     app.run(debug=True, port=5001, host='127.0.0.1')






from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import unquote
import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ======================
# DATABASE MODELS
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
    image = db.Column(db.String(500))

# ======================
# 🥗 EXTENDED RECIPES (Cuisine-specific!)
# ======================
DEMO_RECIPES = [
    # ASIAN
    {"recipe_name": "Chicken Fried Rice 🇨🇳", "ingredients_list": "chicken, rice, eggs, peas, soy sauce", "image_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400", "cuisine": "chinese", "calories": 420, "protein": 25, "carbohydrates": 55, "fat": 15},
    {"recipe_name": "Veggie Spring Rolls 🥡", "ingredients_list": "rice paper, veggies, tofu, peanut sauce", "image_url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400", "cuisine": "chinese", "calories": 280, "protein": 12, "carbohydrates": 45, "fat": 8},
    {"recipe_name": "Teriyaki Tofu 🍜", "ingredients_list": "tofu, broccoli, teriyaki sauce, rice", "image_url": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400", "cuisine": "japanese", "calories": 350, "protein": 18, "carbohydrates": 50, "fat": 10},
    
    # MEDITERRANEAN  
    {"recipe_name": "Greek Chicken Salad 🇬🇷", "ingredients_list": "chicken, feta, olives, cucumber, tzatziki", "image_url": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400", "cuisine": "mediterranean", "calories": 380, "protein": 30, "carbohydrates": 20, "fat": 22},
    {"recipe_name": "Quinoa Falafel Bowl 🥗", "ingredients_list": "falafel, quinoa, hummus, veggies, tahini", "image_url": "https://images.unsplash.com/photo-1511690656952-34342bb7c2f2?w=400", "cuisine": "mediterranean", "calories": 410, "protein": 16, "carbohydrates": 52, "fat": 18},
    
    # THAI
    {"recipe_name": "Thai Green Curry 🌶️", "ingredients_list": "chicken, coconut milk, green curry paste, veggies", "image_url": "https://images.unsplash.com/photo-1571708264037-d52b0a509ee9?w=400", "cuisine": "thai", "calories": 480, "protein": 22, "carbohydrates": 35, "fat": 32},
    {"recipe_name": "Pad Thai Noodles 🍜", "ingredients_list": "rice noodles, shrimp, peanuts, tamarind, sprouts", "image_url": "https://images.unsplash.com/photo-1559314809-0f31657ffa5e?w=400", "cuisine": "thai", "calories": 520, "protein": 28, "carbohydrates": 70, "fat": 18},
    
    # INDIAN
    {"recipe_name": "Butter Chicken 🥘", "ingredients_list": "chicken, butter, cream, tomatoes, spices", "image_url": "https://images.unsplash.com/photo-1568038939894-0b75b7a19631?w=400", "cuisine": "indian", "calories": 550, "protein": 32, "carbohydrates": 25, "fat": 38},
    {"recipe_name": "Chana Masala 🌿", "ingredients_list": "chickpeas, tomatoes, onions, spices, cilantro", "image_url": "https://images.unsplash.com/photo-1603251575712-3d91b6bd461b?w=400", "cuisine": "indian", "calories": 380, "protein": 15, "carbohydrates": 60, "fat": 12},
]

recipes_data = pd.DataFrame(DEMO_RECIPES)

# ======================
# 🔐 AUTH (unchanged)
# ======================



import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAoDQlmaHcfn_7vFddViex6oKAdeOJcT6o")

import google.generativeai as genai

# for m in genai.list_models():
#     print(m.name)
model = genai.GenerativeModel("models/gemini-2.5-flash")
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'user_id' not in session:
        return redirect('/login')

    # 👇 If user opens page
    if request.method == 'GET':
        return render_template('chat.html')

    # 👇 If frontend sends message
    if request.method == 'POST':
        user_message = request.json.get('message', '').strip()

        if not user_message:
            return jsonify({'response': 'Ask something! 🍳'})

        try:
            response = model.generate_content(user_message)
            return jsonify({'response': response.text})

        except Exception as e:
            print("🔥 ERROR:", e)
            return jsonify({'response': "Server error 😅"})











@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect('/')
        return render_template('login.html', error="❌ Invalid!")
    session.clear()
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not User.query.filter_by(username=username).first():
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        return render_template('register.html', error="❌ Exists!")
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ======================
# 🏠 HOME - SMART RECOMMENDATIONS!
# ======================
@app.route('/', methods=['GET', 'POST'])
def home():
    if 'user_id' not in session:
        return redirect('/login')

    recommendations = []
    form_data = {}

    # ✅ GET: Show empty OR restore from session
    if request.method == 'GET':
        # Check if we have valid recommendations in session
        search_hash = session.get('search_hash')
        if search_hash:
            # Restore recommendations
            rec_ids = session.get('rec_ids', [])
            for idx in rec_ids[:3]:
                if idx < len(recipes_data):
                    recipe = recipes_data.iloc[idx]
                    recommendations.append({
                        'recipe_name': recipe['recipe_name'],
                        'ingredients_list': recipe['ingredients_list'],
                        'image_url': recipe['image_url'],
                        'cuisine': recipe['cuisine'],
                        'calories': int(recipe['calories']),
                        'protein': float(recipe['protein']),
                        'carbohydrates': float(recipe['carbohydrates']),
                        'fat': float(recipe['fat'])
                    })
            form_data = session.get('form_data', {})
        return render_template('index.html', recommendations=recommendations, form_data=form_data)

    # ✅ POST: Generate FRESH recommendations
    if request.method == 'POST':
        print("🔥 NEW SMART SEARCH!")
        
        ingredients = request.form.get('ingredients', '').lower().strip()
        cuisine = request.form.get('cuisine', '').lower().strip()
        calories = float(request.form.get('calories', 400))
        protein = float(request.form.get('protein', 20))
        fat = float(request.form.get('fat', 15))
        carbs = float(request.form.get('carbohydrates', 50))

        print(f"📊 Ingredients: '{ingredients}' | Cuisine: '{cuisine}' | {calories}cal")

        matches = []
        for idx, recipe in recipes_data.iterrows():
            score = 0
            r_name = str(recipe['recipe_name']).lower()
            r_ing = str(recipe['ingredients_list']).lower()
            r_cui = str(recipe['cuisine']).lower()
            
            # 🧠 SMART INGREDIENT MATCHING
            ingredient_words = ingredients.split(',')
            for word in ingredient_words:
                word = word.strip()
                if word:
                    if word in r_ing or word in r_name:
                        score += 35  # High priority
                    elif any(syn in r_ing for syn in [word+'s', word+'ed', word+'ing']):
                        score += 20
            
            # 🎯 EXACT CUISINE MATCH (PRIORITY!)
            if cuisine and cuisine in r_cui:
                score += 50  # Cuisine is KING!
            elif not cuisine:
                score += 15  # Bonus for any cuisine
                
            # 📊 NUTRITION MATCHING
            cal_diff = abs(recipe['calories'] - calories) / 100
            score += max(0, 25 - cal_diff * 5)
            
            prot_diff = abs(recipe['protein'] - protein) / 10
            score += max(0, 15 - prot_diff * 3)
            
            fat_diff = abs(recipe['fat'] - fat) / 10
            score += max(0, 10 - fat_diff * 2)

            matches.append({'idx': idx, 'score': score, 'cuisine_match': cuisine in r_cui})

        # 🏆 SORT: Cuisine first, then score!
        matches.sort(key=lambda x: (x['cuisine_match'], x['score']), reverse=True)
        
        # Get TOP 3
        top_indices = [m['idx'] for m in matches[:3]]
        print(f"📈 Top 3 indices: {top_indices} (Cuisine: {cuisine})")

        # Build recommendations
        for idx in top_indices:
            recipe = recipes_data.iloc[idx]
            recommendations.append({
                'recipe_name': recipe['recipe_name'],
                'ingredients_list': recipe['ingredients_list'],
                'image_url': recipe['image_url'],
                'cuisine': recipe['cuisine'],
                'calories': int(recipe['calories']),
                'protein': float(recipe['protein']),
                'carbohydrates': float(recipe['carbohydrates']),
                'fat': float(recipe['fat'])
            })

        # ✅ Store for BACK BUTTON
        session['rec_ids'] = top_indices
        session['search_hash'] = f"{ingredients}_{cuisine}_{calories}"
        session['form_data'] = {k: str(v)[:30] for k, v in request.form.items()}

        print(f"✅ {len(recommendations)} fresh results!")

    form_data = session.get('form_data', {})
    return render_template('index.html', recommendations=recommendations, form_data=form_data)

# ======================
# OTHER ROUTES (unchanged)
# ======================
@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    if 'user_id' not in session: return jsonify({'message': 'Login!'})
    data = request.get_json()
    name = data.get('name', '')[:150]
    if not Cookbook.query.filter_by(user_id=session['user_id'], recipe_name=name).first():
        recipe = Cookbook(user_id=session['user_id'], recipe_name=name,
                         ingredients=data.get('ingredients', '')[:500],
                         image=data.get('image', '')[:200])
        db.session.add(recipe)
        db.session.commit()
    return jsonify({'message': 'Saved ❤️'})

@app.route('/cookbook')
def cookbook():
    if 'user_id' not in session: return redirect('/login')
    recipes = Cookbook.query.filter_by(user_id=session['user_id']).all()
    return render_template('cookbook.html', recipes=recipes)

# @app.route('/recipe/<path:name>')
# def recipe_detail(name):
#     if 'user_id' not in session: return redirect('/login')
#     name = unquote(name)
#     for _, recipe in recipes_data.iterrows():
#         if recipe['recipe_name'] == name:
#             return render_template('recipe_detail.html', 
#                                  recipe=recipe.to_dict(),
#                                  instructions="""<ol><li>Gather ingredients</li><li>Heat oil</li><li>Cook 5-7 mins</li><li>Add spices</li><li>Simmer</li><li>Serve!</li></ol>""")
#     return "Not found", 404

@app.route('/recipe/<path:name>')
def recipe_detail(name):
    if 'user_id' not in session:
        return redirect('/login')
    
    name = unquote(name)
    
    # Find recipe
    for _, recipe_row in recipes_data.iterrows():
        if recipe_row['recipe_name'] == name:
            recipe = recipe_row.to_dict()
            
            # ✅ PROPER HTML INSTRUCTIONS
            instructions = f"""
            <div class="row g-3 mb-4">
                <div class="col-md-6">
                    <div class="card border-0 shadow-sm">
                        <div class="card-body">
                            <h6 class="card-title text-success mb-3">
                                <i class="fas fa-fire me-2"></i>Quick Steps
                            </h6>
                            <ol class="list-group list-group-numbered list-group-flush">
                                <li class="list-group-item px-0 border-0 py-2">
                                    <i class="fas fa-shopping-basket text-primary me-2"></i>
                                    Gather all ingredients
                                </li>
                                <li class="list-group-item px-0 border-0 py-2">
                                    <i class="fas fa-fire text-warning me-2"></i>
                                    Heat 1-2 tbsp oil (medium heat)
                                </li>
                                <li class="list-group-item px-0 border-0 py-2">
                                    <i class="fas fa-drumstick-bite text-danger me-2"></i>
                                    Cook protein/veggies 5-7 mins
                                </li>
                                <li class="list-group-item px-0 border-0 py-2">
                                    <i class="fas fa-pepper-hot text-orange me-2"></i>
                                    Add sauces & spices
                                </li>
                                <li class="list-group-item px-0 border-0 py-2">
                                    <i class="fas fa-clock text-info me-2"></i>
                                    Simmer covered 8-12 mins
                                </li>
                                <li class="list-group-item px-0 border-0 py-2 fw-bold">
                                    <i class="fas fa-plate-wheat text-success me-2"></i>
                                    Serve hot & enjoy! 🌟
                                </li>
                            </ol>
                        </div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card border-0 shadow-sm h-100">
                        <div class="card-body">
                            <h6 class="card-title text-primary mb-3">
                                <i class="fas fa-lightbulb me-2"></i>Pro Tips
                            </h6>
                            <ul class="list-unstyled">
                                <li><i class="fas fa-check-circle text-success me-2"></i>Prep time: 10 mins</li>
                                <li><i class="fas fa-check-circle text-success me-2"></i>Cook time: 20 mins</li>
                                <li><i class="fas fa-check-circle text-success me-2"></i>Serves: 2-4 people</li>
                                <li><i class="fas fa-check-circle text-success me-2"></i>Difficulty: Easy</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            """
            return render_template('recipe_detail.html', recipe=recipe, instructions=instructions)
    
    return "Recipe not found ❌", 404



@app.route('/delete_recipe/<int:id>', methods=['POST'])
def delete_recipe(id):
    if 'user_id' not in session: return jsonify({'message': 'Login!'})
    recipe = Cookbook.query.get(id)
    if recipe and recipe.user_id == session['user_id']:
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': 'Removed 🗑️'})
    return jsonify({'message': 'Not found'})

@app.route('/clear_search')
def clear_search():
    session.pop('rec_ids', None)
    session.pop('search_hash', None)
    session.pop('form_data', None)
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("🚀 SMART RECOMMENDATIONS! http://127.0.0.1:5001")
    app.run(debug=True, port=5001, host='127.0.0.1')