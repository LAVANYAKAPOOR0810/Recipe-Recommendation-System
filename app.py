from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)



# Absolute path example
data = pd.read_csv("recipe_final1.csv")

# Preprocess Ingredients
vectorizer = TfidfVectorizer()
X_ingredients = vectorizer.fit_transform(data['ingredients_list'])

# Normalize Numerical Features
scaler = StandardScaler()
X_numerical = scaler.fit_transform(data[['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']])

# Combine Features
X_combined = np.hstack([X_numerical, X_ingredients.toarray()])

# Train KNN Model
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(X_combined)

def recommend_recipes(input_features):
    input_features_scaled = scaler.transform([input_features[:7]])
    input_ingredients_transformed = vectorizer.transform([input_features[7]])
    input_combined = np.hstack([input_features_scaled, input_ingredients_transformed.toarray()])
    distances, indices = knn.kneighbors(input_combined)
    recommendations = data.iloc[indices[0]]
    return recommendations[['recipe_name', 'ingredients_list', 'image_url',
                        'calories', 'fat', 'carbohydrates', 
                        'protein', 'fiber']].head(5)

# Function to truncate product name
def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        calories = float(request.form['calories'])
        fat = float(request.form['fat'])
        carbohydrates = float(request.form['carbohydrates'])
        protein = float(request.form['protein'])
        cholesterol = float(request.form['cholesterol'])
        sodium = float(request.form['sodium'])
        fiber = float(request.form['fiber'])
        ingredients = request.form['ingredients']
        input_features = [calories, fat, carbohydrates, protein, cholesterol, sodium, fiber, ingredients]
        recommendations = recommend_recipes(input_features)
        return render_template('index.html', recommendations=recommendations.to_dict(orient='records'),truncate = truncate)
    return render_template('index.html', recommendations=[])

@app.route('/cookbook')
def cookbook():
    return render_template('cookbook.html')


if __name__ == '__main__':
    app.run(debug=True)










# from flask import Flask, render_template, request
# import numpy as np
# import pandas as pd
# from sklearn.neighbors import NearestNeighbors
# from sklearn.preprocessing import StandardScaler
# from sklearn.feature_extraction.text import TfidfVectorizer
# import os

# app = Flask(__name__)

# # Load and preprocess data (only once)
# print("Loading dataset...")
# try:
#     data = pd.read_csv("recipe_final1.csv")
#     print(f"Dataset loaded: {len(data)} recipes")
# except FileNotFoundError:
#     print("ERROR: recipe_final1.csv not found!")
#     data = pd.DataFrame()

# if not data.empty:
#     # Preprocess Ingredients
#     print("Vectorizing ingredients...")
#     vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
#     X_ingredients = vectorizer.fit_transform(data['ingredients_list'].fillna(''))

#     # Normalize Numerical Features
#     print("Scaling numerical features...")
#     numerical_cols = ['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']
#     X_numerical = StandardScaler().fit_transform(data[numerical_cols].fillna(0))

#     # Combine Features
#     X_combined = np.hstack([X_numerical, X_ingredients.toarray()])

#     # Train KNN Model
#     print("Training KNN model...")
#     knn = NearestNeighbors(n_neighbors=6, metric='euclidean', algorithm='auto')
#     knn.fit(X_combined)
#     print("✅ Model ready!")
# else:
#     vectorizer = None
#     knn = None
#     print("⚠️ No data loaded - using dummy recommendations")

# def recommend_recipes(input_features):
#     if knn is None or data.empty:
#         # Dummy recommendations if no data
#         return pd.DataFrame([{
#             'recipe_name': 'Sample Recipe',
#             'ingredients_list': 'chicken, rice, vegetables',
#             'image_url': 'https://via.placeholder.com/400x220/4CAF50/FFFFFF?text=Recipe',
#             'calories': 350,
#             'fat': 12,
#             'carbohydrates': 45,
#             'protein': 25,
#             'fiber': 6
#         } for _ in range(3)])
    
#     try:
#         # Extract numerical and text features
#         num_features = input_features[:7]  # calories, fat, carbs, protein, cholesterol, sodium, fiber
#         ingredients_text = input_features[7]
        
#         # Scale numerical features
#         input_num_scaled = StandardScaler().fit_transform([num_features])
        
#         # Transform ingredients
#         input_ingredients = vectorizer.transform([ingredients_text])
        
#         # Combine
#         input_combined = np.hstack([input_num_scaled, input_ingredients.toarray()])
        
#         # Find nearest neighbors
#         distances, indices = knn.kneighbors(input_combined)
        
#         # Get recommendations with full nutrition info
#         recommendations = data.iloc[indices[0]].head(5).copy()
        
#         # Ensure all required columns exist
#         for col in ['calories', 'fat', 'carbohydrates', 'protein', 'fiber']:
#             if col not in recommendations.columns:
#                 recommendations[col] = 0
        
#         # Select and format output
#         result = recommendations[[
#             'recipe_name', 'ingredients_list', 'image_url', 
#             'calories', 'fat', 'carbohydrates', 'protein', 'fiber'
#         ]].fillna({
#             'image_url': 'https://via.placeholder.com/400x220/4CAF50/FFFFFF?text=No+Image',
#             'recipe_name': 'Unknown Recipe'
#         })
        
#         return result.to_dict(orient='records')
    
#     except Exception as e:
#         print(f"Recommendation error: {e}")
#         return []

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     recommendations = []
#     show_results = False
    
#     if request.method == 'POST':
#         try:
#             # Get form data with defaults
#             form_data = {
#                 'calories': float(request.form.get('calories', 0)),
#                 'fat': float(request.form.get('fat', 0)),
#                 'carbohydrates': float(request.form.get('carbohydrates', 0)),
#                 'protein': float(request.form.get('protein', 0)),
#                 'cholesterol': float(request.form.get('cholesterol', 0)),
#                 'sodium': float(request.form.get('sodium', 0)),
#                 'fiber': float(request.form.get('fiber', 0)),
#                 'ingredients': request.form.get('ingredients', '').strip()
#             }
            
#             input_features = [
#                 form_data['calories'], form_data['fat'], form_data['carbohydrates'],
#                 form_data['protein'], form_data['cholesterol'], form_data['sodium'],
#                 form_data['fiber'], form_data['ingredients']
#             ]
            
#             recommendations = recommend_recipes(input_features)
#             show_results = True
            
#             print(f"✅ Found {len(recommendations)} recommendations")
            
#         except Exception as e:
#             print(f"❌ Form error: {e}")
#             show_results = True  # Show "no results" message
    
#     return render_template('index.html', 
#                          recommendations=recommendations, 
#                          show_results=show_results)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)