import pandas as pd
import re
from collections import Counter

# Load your dataset
df = pd.read_csv('recipe_final1.csv')

def detect_cuisine(ingredients, recipe_name):
    """Smart cuisine detector based on ingredients + name"""
    text = f"{recipe_name.lower()} {ingredients.lower()}"
    
    # Cuisine keyword dictionaries
    cuisines = {
        'indian': ['curry', 'tikka', 'masala', 'biryani', 'dal', 'roti', 'naan', 'paneer', 'samosa', 'chutney', 'garam masala', 'tandoori'],
        'chinese': ['soy', 'ginger', 'stir fry', 'wonton', 'dumpling', 'noodle', 'rice', 'chow mein', 'kung pao', 'hoisin'],
        'italian': ['pasta', 'pizza', 'risotto', 'parmesan', 'mozzarella', 'basil', 'tomato', 'pesto', 'gnocchi', 'lasagna'],
        'mexican': ['taco', 'burrito', 'enchilada', 'salsa', 'guacamole', 'chili', 'quesadilla', 'cilantro', 'lime', 'tortilla'],
        'thai': ['coconut milk', 'lemongrass', 'fish sauce', 'pad thai', 'curry paste', 'galangal', 'chili paste', 'satay'],
        'japanese': ['sushi', 'ramen', 'tempura', 'miso', 'soy', 'wasabi', 'teriyaki', 'udon', 'soba', 'tofu'],
        'mediterranean': ['feta', 'hummus', 'falafel', 'couscous', 'olives', 'tzatziki', 'halloumi', 'zaatar'],
        'american': ['burger', 'bbq', 'mac cheese', 'fries', 'hot dog', 'ribs', 'biscuit', 'gravy'],
        'french': ['croissant', 'baguette', 'escargot', 'ratatouille', 'coq au vin', 'béarnaise'],
        'korean': ['kimchi', 'bibimbap', 'bulgogi', 'gochujang', 'korean bbq', 'banchan'],
        'middle_eastern': ['shawarma', 'kebab', 'tabouli', 'baba ganoush', 'sumac'],
        'other': []
    }
    
    scores = {}
    for cuisine, keywords in cuisines.items():
        score = sum(1 for word in keywords if re.search(r'\b' + re.escape(word) + r'\b', text))
        scores[cuisine] = score
    
    # Return highest scoring cuisine
    top_cuisine = max(scores, key=scores.get)
    return top_cuisine if scores[top_cuisine] > 0 else 'other'

# Apply to all recipes (fast!)
print("🔍 Detecting cuisines for 15,000+ recipes...")
df['cuisine'] = df.apply(lambda row: detect_cuisine(row['ingredients_list'], row['recipe_name']), axis=1)

# Save updated dataset
df.to_csv('recipe_final1_with_cuisine.csv', index=False)
print("✅ Saved! Check cuisine distribution:")
print(df['cuisine'].value_counts().head(10))