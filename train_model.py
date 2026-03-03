# import pandas as pd
# import numpy as np
# import pickle
# from sklearn.neighbors import NearestNeighbors
# from sklearn.preprocessing import StandardScaler
# from sklearn.feature_extraction.text import TfidfVectorizer
# from scipy.sparse import hstack, csr_matrix

# # Load dataset
# recipe_df = pd.read_csv("recipe_final(1).csv")

# # TF-IDF for ingredients
# vectorizer = TfidfVectorizer()
# X_ingredients = vectorizer.fit_transform(recipe_df['ingredients_list'])

# # Scale numerical features
# scaler = StandardScaler()
# X_numerical = scaler.fit_transform(
#     recipe_df[['calories', 'fat', 'carbohydrates', 
#                'protein', 'cholesterol', 'sodium', 'fiber']]
# )

# # Convert numerical to sparse
# X_numerical_sparse = csr_matrix(X_numerical)

# # Combine features (IMPORTANT)
# X_combined = hstack([X_ingredients, X_numerical_sparse])

# # Train KNN
# knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
# knn.fit(X_combined)

# # Save everything
# pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
# pickle.dump(scaler, open("scaler.pkl", "wb"))
# pickle.dump(knn, open("knn_model.pkl", "wb"))

# print("Files saved successfully!")







import pandas as pd
import numpy as np
import pickle

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack, csr_matrix

# Load dataset
recipe_df = pd.read_csv("recipe_final1.csv")

# ---------- TEXT FEATURES ----------
vectorizer = TfidfVectorizer()
X_ingredients = vectorizer.fit_transform(recipe_df["ingredients_list"])

# ---------- NUMERICAL FEATURES ----------
scaler = StandardScaler()
X_numerical = scaler.fit_transform(
    recipe_df[["calories", "fat", "carbohydrates", 
               "protein", "cholesterol", "sodium", "fiber"]]
)

# Convert numerical to sparse
X_numerical_sparse = csr_matrix(X_numerical)

# ---------- COMBINE ----------
X_combined = hstack([X_ingredients, X_numerical_sparse])

# ---------- TRAIN MODEL ----------
knn = NearestNeighbors(n_neighbors=3, metric="euclidean")
knn.fit(X_combined)

# ---------- SAVE FILES ----------
pickle.dump(knn, open("recipe_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("Model training complete. Files saved.")