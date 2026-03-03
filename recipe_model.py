{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "d9c9f655-de7a-4fc9-b0c9-a1f1c138fbab",
      "cell_type": "code",
      "source": "import pandas as pd\n\n# Load the dataset\nfile_path = 'recipe_final (1).csv'\nrecipe_df = pd.read_csv(file_path)\n\nrecipe_df.head()",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 4,
          "output_type": "execute_result",
          "data": {
            "text/plain": "   Unnamed: 0  recipe_id                        recipe_name  aver_rate  \\\n0           0     222388                     Homemade Bacon       5.00   \n1           1     240488  Pork Loin, Apples, and Sauerkraut       4.76   \n2           2     218939   Foolproof Rosemary Chicken Wings       4.57   \n3           3      87211              Chicken Pesto Paninis       4.62   \n4           4     245714                 Potato Bacon Pizza       4.50   \n\n                                           image_url  review_nums  calories  \\\n0  https://images.media-allrecipes.com/userphotos...            3        15   \n1  https://images.media-allrecipes.com/userphotos...           29        19   \n2  https://images.media-allrecipes.com/userphotos...           12        17   \n3  https://images.media-allrecipes.com/userphotos...          163        32   \n4  https://images.media-allrecipes.com/userphotos...            2         8   \n\n   fat  carbohydrates  protein  cholesterol  sodium  fiber  \\\n0   36              1       42           21      81      2   \n1   18             10       73           33     104     41   \n2   36              2       48           24      31      4   \n3   45             20       65           20      43     18   \n4   12              5       14            7       8      3   \n\n                                    ingredients_list  \n0  ['pork belly', 'smoked paprika', 'kosher salt'...  \n1  ['sauerkraut drained', 'Granny Smith apples sl...  \n2  ['chicken wings', 'sprigs rosemary', 'head gar...  \n3  ['focaccia bread quartered', 'prepared basil p...  \n4  ['red potatoes', 'strips bacon', 'Sauce:', 'he...  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>recipe_id</th>\n      <th>recipe_name</th>\n      <th>aver_rate</th>\n      <th>image_url</th>\n      <th>review_nums</th>\n      <th>calories</th>\n      <th>fat</th>\n      <th>carbohydrates</th>\n      <th>protein</th>\n      <th>cholesterol</th>\n      <th>sodium</th>\n      <th>fiber</th>\n      <th>ingredients_list</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>0</td>\n      <td>222388</td>\n      <td>Homemade Bacon</td>\n      <td>5.00</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>3</td>\n      <td>15</td>\n      <td>36</td>\n      <td>1</td>\n      <td>42</td>\n      <td>21</td>\n      <td>81</td>\n      <td>2</td>\n      <td>['pork belly', 'smoked paprika', 'kosher salt'...</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>240488</td>\n      <td>Pork Loin, Apples, and Sauerkraut</td>\n      <td>4.76</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>29</td>\n      <td>19</td>\n      <td>18</td>\n      <td>10</td>\n      <td>73</td>\n      <td>33</td>\n      <td>104</td>\n      <td>41</td>\n      <td>['sauerkraut drained', 'Granny Smith apples sl...</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2</td>\n      <td>218939</td>\n      <td>Foolproof Rosemary Chicken Wings</td>\n      <td>4.57</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>12</td>\n      <td>17</td>\n      <td>36</td>\n      <td>2</td>\n      <td>48</td>\n      <td>24</td>\n      <td>31</td>\n      <td>4</td>\n      <td>['chicken wings', 'sprigs rosemary', 'head gar...</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3</td>\n      <td>87211</td>\n      <td>Chicken Pesto Paninis</td>\n      <td>4.62</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>163</td>\n      <td>32</td>\n      <td>45</td>\n      <td>20</td>\n      <td>65</td>\n      <td>20</td>\n      <td>43</td>\n      <td>18</td>\n      <td>['focaccia bread quartered', 'prepared basil p...</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>4</td>\n      <td>245714</td>\n      <td>Potato Bacon Pizza</td>\n      <td>4.50</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>2</td>\n      <td>8</td>\n      <td>12</td>\n      <td>5</td>\n      <td>14</td>\n      <td>7</td>\n      <td>8</td>\n      <td>3</td>\n      <td>['red potatoes', 'strips bacon', 'Sauce:', 'he...</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 4
    },
    {
      "id": "85433606-6bac-437a-84a9-55c6ed64e085",
      "cell_type": "code",
      "source": "import os\nprint(os.getcwd())\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "/drive\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "80054bc3-a487-4388-b10f-d55a99bc7d2e",
      "cell_type": "code",
      "source": "# import os\n# os.listdir()",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 3
    },
    {
      "id": "6a6db2a4-38d5-4e6a-802f-3872bb6c7cc6",
      "cell_type": "code",
      "source": "recipe_df.isnull().sum()",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 30,
          "output_type": "execute_result",
          "data": {
            "text/plain": "Unnamed: 0          0\nrecipe_id           0\nrecipe_name         0\naver_rate           0\nimage_url           0\nreview_nums         0\ncalories            0\nfat                 0\ncarbohydrates       0\nprotein             0\ncholesterol         0\nsodium              0\nfiber               0\ningredients_list    0\ndtype: int64"
          },
          "metadata": {}
        }
      ],
      "execution_count": 30
    },
    {
      "id": "e54e205d-206d-42a3-af35-8598b8280b06",
      "cell_type": "code",
      "source": "recipe_df['ingredients_list'][0]",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 5,
          "output_type": "execute_result",
          "data": {
            "text/plain": "\"['pork belly', 'smoked paprika', 'kosher salt', 'ground black pepper']\""
          },
          "metadata": {}
        }
      ],
      "execution_count": 5
    },
    {
      "id": "f859d12e-3307-4403-80dc-4077eb9a262a",
      "cell_type": "code",
      "source": "import numpy as np\nfrom sklearn.neighbors import NearestNeighbors\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.feature_extraction.text import TfidfVectorizer\n# from sklearn.pipeline import Pipeline",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 6
    },
    {
      "id": "cf53d650-425b-432e-8060-e3cd8487590b",
      "cell_type": "code",
      "source": "# Preprocess Ingredients\nvectorizer = TfidfVectorizer()\nX_ingredients = vectorizer.fit_transform(recipe_df['ingredients_list'])",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 7
    },
    {
      "id": "21433358-991d-413f-bfa7-1bb09b2f1b96",
      "cell_type": "code",
      "source": "recipe_df",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 8,
          "output_type": "execute_result",
          "data": {
            "text/plain": "       Unnamed: 0  recipe_id                        recipe_name  aver_rate  \\\n0               0     222388                     Homemade Bacon       5.00   \n1               1     240488  Pork Loin, Apples, and Sauerkraut       4.76   \n2               2     218939   Foolproof Rosemary Chicken Wings       4.57   \n3               3      87211              Chicken Pesto Paninis       4.62   \n4               4     245714                 Potato Bacon Pizza       4.50   \n...           ...        ...                                ...        ...   \n48730       48730     222886             Grateful Dead Cocktail       3.50   \n48731       48731      25650        Cheese Filling For Pastries       4.33   \n48732       48732      23544                     Peach Smoothie       3.62   \n48733       48733     170710                Double Dare Peaches       4.71   \n48734       48734      79774         All-Purpose Marinara Sauce       4.50   \n\n                                               image_url  review_nums  \\\n0      https://images.media-allrecipes.com/userphotos...            3   \n1      https://images.media-allrecipes.com/userphotos...           29   \n2      https://images.media-allrecipes.com/userphotos...           12   \n3      https://images.media-allrecipes.com/userphotos...          163   \n4      https://images.media-allrecipes.com/userphotos...            2   \n...                                                  ...          ...   \n48730  https://images.media-allrecipes.com/userphotos...            4   \n48731  https://images.media-allrecipes.com/userphotos...            3   \n48732  https://images.media-allrecipes.com/userphotos...           21   \n48733  https://images.media-allrecipes.com/userphotos...           19   \n48734  https://images.media-allrecipes.com/userphotos...            2   \n\n       calories  fat  carbohydrates  protein  cholesterol  sodium  fiber  \\\n0            15   36              1       42           21      81      2   \n1            19   18             10       73           33     104     41   \n2            17   36              2       48           24      31      4   \n3            32   45             20       65           20      43     18   \n4             8   12              5       14            7       8      3   \n...         ...  ...            ...      ...          ...     ...    ...   \n48730        20    1              6        1            0       1      0   \n48731         6   14              2        4           13       3      1   \n48732         8    7              8       10            3       3      8   \n48733        20   33             16       11           25       7      5   \n48734         2    3              2        3            0      16      6   \n\n                                        ingredients_list  \n0      ['pork belly', 'smoked paprika', 'kosher salt'...  \n1      ['sauerkraut drained', 'Granny Smith apples sl...  \n2      ['chicken wings', 'sprigs rosemary', 'head gar...  \n3      ['focaccia bread quartered', 'prepared basil p...  \n4      ['red potatoes', 'strips bacon', 'Sauce:', 'he...  \n...                                                  ...  \n48730  ['fluid ounce tequila', 'fluid ounce vodka', '...  \n48731  ['raisins', 'brandy', 'cream cheese', 'white s...  \n48732  ['sliced peaches drained', 'scoops vanilla ice...  \n48733  ['butter', 'habanero peppers', 'fresh peaches'...  \n48734  ['olive oil', 'bulb garlic', 'tomatoes chopped...  \n\n[48735 rows x 14 columns]",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>recipe_id</th>\n      <th>recipe_name</th>\n      <th>aver_rate</th>\n      <th>image_url</th>\n      <th>review_nums</th>\n      <th>calories</th>\n      <th>fat</th>\n      <th>carbohydrates</th>\n      <th>protein</th>\n      <th>cholesterol</th>\n      <th>sodium</th>\n      <th>fiber</th>\n      <th>ingredients_list</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>0</td>\n      <td>222388</td>\n      <td>Homemade Bacon</td>\n      <td>5.00</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>3</td>\n      <td>15</td>\n      <td>36</td>\n      <td>1</td>\n      <td>42</td>\n      <td>21</td>\n      <td>81</td>\n      <td>2</td>\n      <td>['pork belly', 'smoked paprika', 'kosher salt'...</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>240488</td>\n      <td>Pork Loin, Apples, and Sauerkraut</td>\n      <td>4.76</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>29</td>\n      <td>19</td>\n      <td>18</td>\n      <td>10</td>\n      <td>73</td>\n      <td>33</td>\n      <td>104</td>\n      <td>41</td>\n      <td>['sauerkraut drained', 'Granny Smith apples sl...</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2</td>\n      <td>218939</td>\n      <td>Foolproof Rosemary Chicken Wings</td>\n      <td>4.57</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>12</td>\n      <td>17</td>\n      <td>36</td>\n      <td>2</td>\n      <td>48</td>\n      <td>24</td>\n      <td>31</td>\n      <td>4</td>\n      <td>['chicken wings', 'sprigs rosemary', 'head gar...</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3</td>\n      <td>87211</td>\n      <td>Chicken Pesto Paninis</td>\n      <td>4.62</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>163</td>\n      <td>32</td>\n      <td>45</td>\n      <td>20</td>\n      <td>65</td>\n      <td>20</td>\n      <td>43</td>\n      <td>18</td>\n      <td>['focaccia bread quartered', 'prepared basil p...</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>4</td>\n      <td>245714</td>\n      <td>Potato Bacon Pizza</td>\n      <td>4.50</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>2</td>\n      <td>8</td>\n      <td>12</td>\n      <td>5</td>\n      <td>14</td>\n      <td>7</td>\n      <td>8</td>\n      <td>3</td>\n      <td>['red potatoes', 'strips bacon', 'Sauce:', 'he...</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>48730</th>\n      <td>48730</td>\n      <td>222886</td>\n      <td>Grateful Dead Cocktail</td>\n      <td>3.50</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>4</td>\n      <td>20</td>\n      <td>1</td>\n      <td>6</td>\n      <td>1</td>\n      <td>0</td>\n      <td>1</td>\n      <td>0</td>\n      <td>['fluid ounce tequila', 'fluid ounce vodka', '...</td>\n    </tr>\n    <tr>\n      <th>48731</th>\n      <td>48731</td>\n      <td>25650</td>\n      <td>Cheese Filling For Pastries</td>\n      <td>4.33</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>3</td>\n      <td>6</td>\n      <td>14</td>\n      <td>2</td>\n      <td>4</td>\n      <td>13</td>\n      <td>3</td>\n      <td>1</td>\n      <td>['raisins', 'brandy', 'cream cheese', 'white s...</td>\n    </tr>\n    <tr>\n      <th>48732</th>\n      <td>48732</td>\n      <td>23544</td>\n      <td>Peach Smoothie</td>\n      <td>3.62</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>21</td>\n      <td>8</td>\n      <td>7</td>\n      <td>8</td>\n      <td>10</td>\n      <td>3</td>\n      <td>3</td>\n      <td>8</td>\n      <td>['sliced peaches drained', 'scoops vanilla ice...</td>\n    </tr>\n    <tr>\n      <th>48733</th>\n      <td>48733</td>\n      <td>170710</td>\n      <td>Double Dare Peaches</td>\n      <td>4.71</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>19</td>\n      <td>20</td>\n      <td>33</td>\n      <td>16</td>\n      <td>11</td>\n      <td>25</td>\n      <td>7</td>\n      <td>5</td>\n      <td>['butter', 'habanero peppers', 'fresh peaches'...</td>\n    </tr>\n    <tr>\n      <th>48734</th>\n      <td>48734</td>\n      <td>79774</td>\n      <td>All-Purpose Marinara Sauce</td>\n      <td>4.50</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n      <td>2</td>\n      <td>2</td>\n      <td>3</td>\n      <td>2</td>\n      <td>3</td>\n      <td>0</td>\n      <td>16</td>\n      <td>6</td>\n      <td>['olive oil', 'bulb garlic', 'tomatoes chopped...</td>\n    </tr>\n  </tbody>\n</table>\n<p>48735 rows × 14 columns</p>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 8
    },
    {
      "id": "5fb6d987-7de2-4fda-8fa0-90e6505da8e8",
      "cell_type": "code",
      "source": "# Normalize Numerical Features\nscaler = StandardScaler()\nX_numerical = scaler.fit_transform(recipe_df[['calories', 'fat', 'carbohydrates', 'protein', 'cholesterol', 'sodium', 'fiber']])",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 9
    },
    {
      "id": "fe59ebe0-fc74-44b5-8ad0-68c46f6b3d3b",
      "cell_type": "code",
      "source": "X_numerical",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 10,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([[-0.1317045 ,  0.46001924, -1.15482863, ...,  0.04256474,\n         1.13990476, -0.76393724],\n       [ 0.23857551, -0.33625589, -0.01920347, ...,  0.52871248,\n         1.59202345,  2.53220175],\n       [ 0.05343551,  0.46001924, -1.02864806, ...,  0.16410167,\n         0.15703804, -0.59490447],\n       ...,\n       [-0.77969453, -0.82286847, -0.27156462, ..., -0.68665688,\n        -0.39336732, -0.25683894],\n       [ 0.33114552,  0.32730672,  0.73787996, ...,  0.20461398,\n        -0.31473798, -0.51038809],\n       [-1.33511455, -0.9998185 , -1.02864806, ..., -0.80819381,\n        -0.13782197, -0.42587171]], shape=(48735, 7))"
          },
          "metadata": {}
        }
      ],
      "execution_count": 10
    },
    {
      "id": "699d6852-fc29-4094-82d0-160e5b302b80",
      "cell_type": "code",
      "source": "\n# Combine Features\n# X_combined = np.hstack([X_numerical, X_ingredients.toarray()])\n# X_combined\n\n\n\n# from scipy.sparse import csr_matrix\n\n# X_numerical_sparse = csr_matrix(X_numerical)\n\n# X_combined = hstack([X_ingredients, X_numerical_sparse])\n\n\nfrom scipy.sparse import hstack\n\nX_combined = hstack([X_ingredients, X_numerical_sparse])",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 12
    },
    {
      "id": "8775a0ca-4934-420b-b456-ada3eac1487f",
      "cell_type": "code",
      "source": "X_combined",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 13,
          "output_type": "execute_result",
          "data": {
            "text/plain": "<Compressed Sparse Row sparse matrix of dtype 'float64'\n\twith 1340651 stored elements and shape (48735, 4905)>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 13
    },
    {
      "id": "18195581-beee-4124-9c48-506473c5b83e",
      "cell_type": "code",
      "source": " # Train KNN Model\nknn = NearestNeighbors(n_neighbors=3, metric='euclidean')\nknn.fit(X_combined)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "NearestNeighbors(metric='euclidean', n_neighbors=3)",
            "text/html": "<style>#sk-container-id-1 {\n  /* Definition of color scheme common for light and dark mode */\n  --sklearn-color-text: #000;\n  --sklearn-color-text-muted: #666;\n  --sklearn-color-line: gray;\n  /* Definition of color scheme for unfitted estimators */\n  --sklearn-color-unfitted-level-0: #fff5e6;\n  --sklearn-color-unfitted-level-1: #f6e4d2;\n  --sklearn-color-unfitted-level-2: #ffe0b3;\n  --sklearn-color-unfitted-level-3: chocolate;\n  /* Definition of color scheme for fitted estimators */\n  --sklearn-color-fitted-level-0: #f0f8ff;\n  --sklearn-color-fitted-level-1: #d4ebff;\n  --sklearn-color-fitted-level-2: #b3dbfd;\n  --sklearn-color-fitted-level-3: cornflowerblue;\n\n  /* Specific color for light theme */\n  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n  --sklearn-color-icon: #696969;\n\n  @media (prefers-color-scheme: dark) {\n    /* Redefinition of color scheme for dark theme */\n    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n    --sklearn-color-icon: #878787;\n  }\n}\n\n#sk-container-id-1 {\n  color: var(--sklearn-color-text);\n}\n\n#sk-container-id-1 pre {\n  padding: 0;\n}\n\n#sk-container-id-1 input.sk-hidden--visually {\n  border: 0;\n  clip: rect(1px 1px 1px 1px);\n  clip: rect(1px, 1px, 1px, 1px);\n  height: 1px;\n  margin: -1px;\n  overflow: hidden;\n  padding: 0;\n  position: absolute;\n  width: 1px;\n}\n\n#sk-container-id-1 div.sk-dashed-wrapped {\n  border: 1px dashed var(--sklearn-color-line);\n  margin: 0 0.4em 0.5em 0.4em;\n  box-sizing: border-box;\n  padding-bottom: 0.4em;\n  background-color: var(--sklearn-color-background);\n}\n\n#sk-container-id-1 div.sk-container {\n  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n     but bootstrap.min.css set `[hidden] { display: none !important; }`\n     so we also need the `!important` here to be able to override the\n     default hidden behavior on the sphinx rendered scikit-learn.org.\n     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n  display: inline-block !important;\n  position: relative;\n}\n\n#sk-container-id-1 div.sk-text-repr-fallback {\n  display: none;\n}\n\ndiv.sk-parallel-item,\ndiv.sk-serial,\ndiv.sk-item {\n  /* draw centered vertical line to link estimators */\n  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n  background-size: 2px 100%;\n  background-repeat: no-repeat;\n  background-position: center center;\n}\n\n/* Parallel-specific style estimator block */\n\n#sk-container-id-1 div.sk-parallel-item::after {\n  content: \"\";\n  width: 100%;\n  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n  flex-grow: 1;\n}\n\n#sk-container-id-1 div.sk-parallel {\n  display: flex;\n  align-items: stretch;\n  justify-content: center;\n  background-color: var(--sklearn-color-background);\n  position: relative;\n}\n\n#sk-container-id-1 div.sk-parallel-item {\n  display: flex;\n  flex-direction: column;\n}\n\n#sk-container-id-1 div.sk-parallel-item:first-child::after {\n  align-self: flex-end;\n  width: 50%;\n}\n\n#sk-container-id-1 div.sk-parallel-item:last-child::after {\n  align-self: flex-start;\n  width: 50%;\n}\n\n#sk-container-id-1 div.sk-parallel-item:only-child::after {\n  width: 0;\n}\n\n/* Serial-specific style estimator block */\n\n#sk-container-id-1 div.sk-serial {\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  background-color: var(--sklearn-color-background);\n  padding-right: 1em;\n  padding-left: 1em;\n}\n\n\n/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\nclickable and can be expanded/collapsed.\n- Pipeline and ColumnTransformer use this feature and define the default style\n- Estimators will overwrite some part of the style using the `sk-estimator` class\n*/\n\n/* Pipeline and ColumnTransformer style (default) */\n\n#sk-container-id-1 div.sk-toggleable {\n  /* Default theme specific background. It is overwritten whether we have a\n  specific estimator or a Pipeline/ColumnTransformer */\n  background-color: var(--sklearn-color-background);\n}\n\n/* Toggleable label */\n#sk-container-id-1 label.sk-toggleable__label {\n  cursor: pointer;\n  display: flex;\n  width: 100%;\n  margin-bottom: 0;\n  padding: 0.5em;\n  box-sizing: border-box;\n  text-align: center;\n  align-items: start;\n  justify-content: space-between;\n  gap: 0.5em;\n}\n\n#sk-container-id-1 label.sk-toggleable__label .caption {\n  font-size: 0.6rem;\n  font-weight: lighter;\n  color: var(--sklearn-color-text-muted);\n}\n\n#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n  /* Arrow on the left of the label */\n  content: \"▸\";\n  float: left;\n  margin-right: 0.25em;\n  color: var(--sklearn-color-icon);\n}\n\n#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n  color: var(--sklearn-color-text);\n}\n\n/* Toggleable content - dropdown */\n\n#sk-container-id-1 div.sk-toggleable__content {\n  display: none;\n  text-align: left;\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-0);\n}\n\n#sk-container-id-1 div.sk-toggleable__content.fitted {\n  /* fitted */\n  background-color: var(--sklearn-color-fitted-level-0);\n}\n\n#sk-container-id-1 div.sk-toggleable__content pre {\n  margin: 0.2em;\n  border-radius: 0.25em;\n  color: var(--sklearn-color-text);\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-0);\n}\n\n#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n  /* unfitted */\n  background-color: var(--sklearn-color-fitted-level-0);\n}\n\n#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n  /* Expand drop-down */\n  display: block;\n  width: 100%;\n  overflow: visible;\n}\n\n#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n  content: \"▾\";\n}\n\n/* Pipeline/ColumnTransformer-specific style */\n\n#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n  color: var(--sklearn-color-text);\n  background-color: var(--sklearn-color-unfitted-level-2);\n}\n\n#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n  background-color: var(--sklearn-color-fitted-level-2);\n}\n\n/* Estimator-specific style */\n\n/* Colorize estimator box */\n#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-2);\n}\n\n#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n  /* fitted */\n  background-color: var(--sklearn-color-fitted-level-2);\n}\n\n#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n#sk-container-id-1 div.sk-label label {\n  /* The background is the default theme color */\n  color: var(--sklearn-color-text-on-default-background);\n}\n\n/* On hover, darken the color of the background */\n#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n  color: var(--sklearn-color-text);\n  background-color: var(--sklearn-color-unfitted-level-2);\n}\n\n/* Label box, darken color on hover, fitted */\n#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n  color: var(--sklearn-color-text);\n  background-color: var(--sklearn-color-fitted-level-2);\n}\n\n/* Estimator label */\n\n#sk-container-id-1 div.sk-label label {\n  font-family: monospace;\n  font-weight: bold;\n  display: inline-block;\n  line-height: 1.2em;\n}\n\n#sk-container-id-1 div.sk-label-container {\n  text-align: center;\n}\n\n/* Estimator-specific */\n#sk-container-id-1 div.sk-estimator {\n  font-family: monospace;\n  border: 1px dotted var(--sklearn-color-border-box);\n  border-radius: 0.25em;\n  box-sizing: border-box;\n  margin-bottom: 0.5em;\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-0);\n}\n\n#sk-container-id-1 div.sk-estimator.fitted {\n  /* fitted */\n  background-color: var(--sklearn-color-fitted-level-0);\n}\n\n/* on hover */\n#sk-container-id-1 div.sk-estimator:hover {\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-2);\n}\n\n#sk-container-id-1 div.sk-estimator.fitted:hover {\n  /* fitted */\n  background-color: var(--sklearn-color-fitted-level-2);\n}\n\n/* Specification for estimator info (e.g. \"i\" and \"?\") */\n\n/* Common style for \"i\" and \"?\" */\n\n.sk-estimator-doc-link,\na:link.sk-estimator-doc-link,\na:visited.sk-estimator-doc-link {\n  float: right;\n  font-size: smaller;\n  line-height: 1em;\n  font-family: monospace;\n  background-color: var(--sklearn-color-background);\n  border-radius: 1em;\n  height: 1em;\n  width: 1em;\n  text-decoration: none !important;\n  margin-left: 0.5em;\n  text-align: center;\n  /* unfitted */\n  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n  color: var(--sklearn-color-unfitted-level-1);\n}\n\n.sk-estimator-doc-link.fitted,\na:link.sk-estimator-doc-link.fitted,\na:visited.sk-estimator-doc-link.fitted {\n  /* fitted */\n  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n  color: var(--sklearn-color-fitted-level-1);\n}\n\n/* On hover */\ndiv.sk-estimator:hover .sk-estimator-doc-link:hover,\n.sk-estimator-doc-link:hover,\ndiv.sk-label-container:hover .sk-estimator-doc-link:hover,\n.sk-estimator-doc-link:hover {\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-3);\n  color: var(--sklearn-color-background);\n  text-decoration: none;\n}\n\ndiv.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n.sk-estimator-doc-link.fitted:hover,\ndiv.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n.sk-estimator-doc-link.fitted:hover {\n  /* fitted */\n  background-color: var(--sklearn-color-fitted-level-3);\n  color: var(--sklearn-color-background);\n  text-decoration: none;\n}\n\n/* Span, style for the box shown on hovering the info icon */\n.sk-estimator-doc-link span {\n  display: none;\n  z-index: 9999;\n  position: relative;\n  font-weight: normal;\n  right: .2ex;\n  padding: .5ex;\n  margin: .5ex;\n  width: min-content;\n  min-width: 20ex;\n  max-width: 50ex;\n  color: var(--sklearn-color-text);\n  box-shadow: 2pt 2pt 4pt #999;\n  /* unfitted */\n  background: var(--sklearn-color-unfitted-level-0);\n  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n}\n\n.sk-estimator-doc-link.fitted span {\n  /* fitted */\n  background: var(--sklearn-color-fitted-level-0);\n  border: var(--sklearn-color-fitted-level-3);\n}\n\n.sk-estimator-doc-link:hover span {\n  display: block;\n}\n\n/* \"?\"-specific style due to the `<a>` HTML tag */\n\n#sk-container-id-1 a.estimator_doc_link {\n  float: right;\n  font-size: 1rem;\n  line-height: 1em;\n  font-family: monospace;\n  background-color: var(--sklearn-color-background);\n  border-radius: 1rem;\n  height: 1rem;\n  width: 1rem;\n  text-decoration: none;\n  /* unfitted */\n  color: var(--sklearn-color-unfitted-level-1);\n  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n}\n\n#sk-container-id-1 a.estimator_doc_link.fitted {\n  /* fitted */\n  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n  color: var(--sklearn-color-fitted-level-1);\n}\n\n/* On hover */\n#sk-container-id-1 a.estimator_doc_link:hover {\n  /* unfitted */\n  background-color: var(--sklearn-color-unfitted-level-3);\n  color: var(--sklearn-color-background);\n  text-decoration: none;\n}\n\n#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n  /* fitted */\n  background-color: var(--sklearn-color-fitted-level-3);\n}\n\n.estimator-table summary {\n    padding: .5rem;\n    font-family: monospace;\n    cursor: pointer;\n}\n\n.estimator-table details[open] {\n    padding-left: 0.1rem;\n    padding-right: 0.1rem;\n    padding-bottom: 0.3rem;\n}\n\n.estimator-table .parameters-table {\n    margin-left: auto !important;\n    margin-right: auto !important;\n}\n\n.estimator-table .parameters-table tr:nth-child(odd) {\n    background-color: #fff;\n}\n\n.estimator-table .parameters-table tr:nth-child(even) {\n    background-color: #f6f6f6;\n}\n\n.estimator-table .parameters-table tr:hover {\n    background-color: #e0e0e0;\n}\n\n.estimator-table table td {\n    border: 1px solid rgba(106, 105, 104, 0.232);\n}\n\n.user-set td {\n    color:rgb(255, 94, 0);\n    text-align: left;\n}\n\n.user-set td.value pre {\n    color:rgb(255, 94, 0) !important;\n    background-color: transparent !important;\n}\n\n.default td {\n    color: black;\n    text-align: left;\n}\n\n.user-set td i,\n.default td i {\n    color: black;\n}\n\n.copy-paste-icon {\n    background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48IS0tIUZvbnQgQXdlc29tZSBGcmVlIDYuNy4yIGJ5IEBmb250YXdlc29tZSAtIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tIExpY2Vuc2UgLSBodHRwczovL2ZvbnRhd2Vzb21lLmNvbS9saWNlbnNlL2ZyZWUgQ29weXJpZ2h0IDIwMjUgRm9udGljb25zLCBJbmMuLS0+PHBhdGggZD0iTTIwOCAwTDMzMi4xIDBjMTIuNyAwIDI0LjkgNS4xIDMzLjkgMTQuMWw2Ny45IDY3LjljOSA5IDE0LjEgMjEuMiAxNC4xIDMzLjlMNDQ4IDMzNmMwIDI2LjUtMjEuNSA0OC00OCA0OGwtMTkyIDBjLTI2LjUgMC00OC0yMS41LTQ4LTQ4bDAtMjg4YzAtMjYuNSAyMS41LTQ4IDQ4LTQ4ek00OCAxMjhsODAgMCAwIDY0LTY0IDAgMCAyNTYgMTkyIDAgMC0zMiA2NCAwIDAgNDhjMCAyNi41LTIxLjUgNDgtNDggNDhMNDggNTEyYy0yNi41IDAtNDgtMjEuNS00OC00OEwwIDE3NmMwLTI2LjUgMjEuNS00OCA0OC00OHoiLz48L3N2Zz4=);\n    background-repeat: no-repeat;\n    background-size: 14px 14px;\n    background-position: 0;\n    display: inline-block;\n    width: 14px;\n    height: 14px;\n    cursor: pointer;\n}\n</style><body><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>NearestNeighbors(metric=&#x27;euclidean&#x27;, n_neighbors=3)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>NearestNeighbors</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.NearestNeighbors.html\">?<span>Documentation for NearestNeighbors</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\" data-param-prefix=\"\">\n        <div class=\"estimator-table\">\n            <details>\n                <summary>Parameters</summary>\n                <table class=\"parameters-table\">\n                  <tbody>\n                    \n        <tr class=\"user-set\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('n_neighbors',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">n_neighbors&nbsp;</td>\n            <td class=\"value\">3</td>\n        </tr>\n    \n\n        <tr class=\"default\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('radius',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">radius&nbsp;</td>\n            <td class=\"value\">1.0</td>\n        </tr>\n    \n\n        <tr class=\"default\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('algorithm',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">algorithm&nbsp;</td>\n            <td class=\"value\">&#x27;auto&#x27;</td>\n        </tr>\n    \n\n        <tr class=\"default\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('leaf_size',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">leaf_size&nbsp;</td>\n            <td class=\"value\">30</td>\n        </tr>\n    \n\n        <tr class=\"user-set\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('metric',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">metric&nbsp;</td>\n            <td class=\"value\">&#x27;euclidean&#x27;</td>\n        </tr>\n    \n\n        <tr class=\"default\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('p',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">p&nbsp;</td>\n            <td class=\"value\">2</td>\n        </tr>\n    \n\n        <tr class=\"default\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('metric_params',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">metric_params&nbsp;</td>\n            <td class=\"value\">None</td>\n        </tr>\n    \n\n        <tr class=\"default\">\n            <td><i class=\"copy-paste-icon\"\n                 onclick=\"copyToClipboard('n_jobs',\n                          this.parentElement.nextElementSibling)\"\n            ></i></td>\n            <td class=\"param\">n_jobs&nbsp;</td>\n            <td class=\"value\">None</td>\n        </tr>\n    \n                  </tbody>\n                </table>\n            </details>\n        </div>\n    </div></div></div></div></div><script>function copyToClipboard(text, element) {\n    // Get the parameter prefix from the closest toggleable content\n    const toggleableContent = element.closest('.sk-toggleable__content');\n    const paramPrefix = toggleableContent ? toggleableContent.dataset.paramPrefix : '';\n    const fullParamName = paramPrefix ? `${paramPrefix}${text}` : text;\n\n    const originalStyle = element.style;\n    const computedStyle = window.getComputedStyle(element);\n    const originalWidth = computedStyle.width;\n    const originalHTML = element.innerHTML.replace('Copied!', '');\n\n    navigator.clipboard.writeText(fullParamName)\n        .then(() => {\n            element.style.width = originalWidth;\n            element.style.color = 'green';\n            element.innerHTML = \"Copied!\";\n\n            setTimeout(() => {\n                element.innerHTML = originalHTML;\n                element.style = originalStyle;\n            }, 2000);\n        })\n        .catch(err => {\n            console.error('Failed to copy:', err);\n            element.style.color = 'red';\n            element.innerHTML = \"Failed!\";\n            setTimeout(() => {\n                element.innerHTML = originalHTML;\n                element.style = originalStyle;\n            }, 2000);\n        });\n    return false;\n}\n\ndocument.querySelectorAll('.fa-regular.fa-copy').forEach(function(element) {\n    const toggleableContent = element.closest('.sk-toggleable__content');\n    const paramPrefix = toggleableContent ? toggleableContent.dataset.paramPrefix : '';\n    const paramName = element.parentElement.nextElementSibling.textContent.trim();\n    const fullParamName = paramPrefix ? `${paramPrefix}${paramName}` : paramName;\n\n    element.setAttribute('title', fullParamName);\n});\n</script></body>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 14
    },
    {
      "id": "51cfae93-849e-421e-b28c-78ac4a92c3f9",
      "cell_type": "code",
      "source": "def recommend_recipes(input_features):\n    input_features_scaled = scaler.transform([input_features[:7]])\n    input_ingredients_transformed = vectorizer.transform([input_features[7]])\n    input_combined = np.hstack([input_features_scaled, input_ingredients_transformed.toarray()])\n    distances, indices = knn.kneighbors(input_combined)\n    recommendations = recipe_df.iloc[indices[0]]\n    return recommendations[['recipe_name', 'ingredients_list', 'image_url']]",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 15
    },
    {
      "id": "590e5d09-8c3f-4b75-a16c-1fc287660da5",
      "cell_type": "code",
      "source": "# Example Input\ninput_features = [15, 36, 1, 42, 21, 81, 2, 'pork belly, smoked paprika, kosher salt']\nrecommendations = recommend_recipes(input_features)\nrecommendations",
      "metadata": {
        "trusted": true,
        "scrolled": true
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": "/lib/python3.13/site-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but StandardScaler was fitted with feature names\n  warnings.warn(\n/lib/python3.13/site-packages/threadpoolctl.py:1123: RuntimeWarning: JsProxy.as_object_map() is deprecated. Use as_py_json() instead.\n  for filepath in LDSO.loadedLibsByName.as_object_map():\n"
        },
        {
          "execution_count": 16,
          "output_type": "execute_result",
          "data": {
            "text/plain": "                  recipe_name  \\\n40002  Caesar Salad Pinwheels   \n27021          Scripture Cake   \n38548   Sweet Onion Casserole   \n\n                                        ingredients_list  \\\n40002  ['cream cheese', 'sun-dried tomatoes in oil', ...   \n27021  ['butter', 'white sugar Jeremiah 6:20', 'eggs ...   \n38548  ['uncooked basmati rice', 'water', 'butter', '...   \n\n                                               image_url  \n40002  https://images.media-allrecipes.com/userphotos...  \n27021  http://images.media-allrecipes.com/userphotos/...  \n38548  https://images.media-allrecipes.com/userphotos...  ",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>recipe_name</th>\n      <th>ingredients_list</th>\n      <th>image_url</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>40002</th>\n      <td>Caesar Salad Pinwheels</td>\n      <td>['cream cheese', 'sun-dried tomatoes in oil', ...</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n    </tr>\n    <tr>\n      <th>27021</th>\n      <td>Scripture Cake</td>\n      <td>['butter', 'white sugar Jeremiah 6:20', 'eggs ...</td>\n      <td>http://images.media-allrecipes.com/userphotos/...</td>\n    </tr>\n    <tr>\n      <th>38548</th>\n      <td>Sweet Onion Casserole</td>\n      <td>['uncooked basmati rice', 'water', 'butter', '...</td>\n      <td>https://images.media-allrecipes.com/userphotos...</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ],
      "execution_count": 16
    },
    {
      "id": "d55f9702-968f-4a85-a3cc-c2f0eecfe16c",
      "cell_type": "code",
      "source": "# import pickle\n# # pickle.dump(tfidf, open(\"tfidf.pkl\", \"wb\"))\n# pickle.dump(recipe_df, open(\"recipes.pkl\", \"wb\"))\n# pickle.dump(similarity, open(\"similarity.pkl\", \"wb\"))",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "id": "05b21de5-392d-49ec-bf9e-66a176ca6bcb",
      "cell_type": "code",
      "source": "%whos",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Variable             Type                Data/Info\n--------------------------------------------------\nNearestNeighbors     ABCMeta             <class 'sklearn.neighbors<...>rvised.NearestNeighbors'>\nStandardScaler       type                <class 'sklearn.preproces<...>ng._data.StandardScaler'>\nTfidfVectorizer      type                <class 'sklearn.feature_e<...>on.text.TfidfVectorizer'>\nX_combined           csr_matrix          <Compressed Sparse Row sp<...>904)\t-0.42587170561458043\nX_ingredients        csr_matrix          <Compressed Sparse Row sp<...>34, 755)\t0.26861975054603\nX_numerical          ndarray             48735x7: 341145 elems, type `float64`, 2729160 bytes (2.6027297973632812 Mb)\nX_numerical_sparse   csr_matrix          <Compressed Sparse Row sp<...>, 6)\t-0.42587170561458043\ncsr_matrix           type                <class 'scipy.sparse._csr.csr_matrix'>\nfile_path            str                 recipe_final (1).csv\nhstack               function            <function hstack at 0xb9bb980>\ninput_features       list                n=8\nknn                  NearestNeighbors    NearestNeighbors(metric='<...>uclidean', n_neighbors=3)\nnp                   module              <module 'numpy' from '/li<...>kages/numpy/__init__.py'>\nos                   module              <module 'os' (frozen)>\npd                   module              <module 'pandas' from '/l<...>ages/pandas/__init__.py'>\nrecipe_df            DataFrame                  Unnamed: 0  recipe<...>[48735 rows x 14 columns]\nrecommend_recipes    function            <function recommend_recipes at 0xe310040>\nrecommendations      DataFrame                             recipe_<...>cipes.com/userphotos...  \nscaler               StandardScaler      StandardScaler()\nvectorizer           TfidfVectorizer     TfidfVectorizer()\n"
        }
      ],
      "execution_count": 17
    },
    {
      "id": "7dec783b-d5f8-4875-9794-89818ef7fa6b",
      "cell_type": "code",
      "source": "import pickle\n\npickle.dump(vectorizer, open(\"vectorizer.pkl\", \"wb\"))\npickle.dump(scaler, open(\"scaler.pkl\", \"wb\"))\n# pickle.dump(knn, open(\"knn_model.pkl\", \"wb\"))\npickle.dump(recipe_df, open(\"recipes.pkl\", \"wb\"))",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 18
    },
    {
      "id": "ec1b35fa-49d1-4fe3-b5f3-0915348d0076",
      "cell_type": "code",
      "source": "pickle.dump(X_combined, open(\"X_combined.pkl\", \"wb\"))",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 19
    },
    {
      "id": "e7d01e19-5ab2-4173-bc67-c6e29cf7348a",
      "cell_type": "code",
      "source": "import os\nprint(os.listdir())",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "['.ipynb', 'LabWork.ipynb', 'Untitled.ipynb', 'Untitled10.ipynb', 'Untitled8.ipynb', 'Untitled9.ipynb', 'X_combined.pkl', 'knn_model.pkl', 'recipe_final (1).csv', 'recipe_recommendation_system.ipynb', 'recipes.pkl', 'scaler.pkl', 'vectorizer.pkl', 'README.md', 'data', 'notebooks']\n"
        }
      ],
      "execution_count": 20
    },
    {
      "id": "f9694452-6b29-46b0-8aa3-64204810d128",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}






import pickle
from scipy.sparse import hstack, csr_matrix

# Load saved objects
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
recipe_df = pickle.load(open("recipes.pkl", "rb"))
knn = pickle.load(open("knn_model.pkl", "rb"))

def recommend_recipes(input_features):
    input_features_scaled = scaler.transform([input_features[:7]])
    input_ingredients_transformed = vectorizer.transform([input_features[7]])

    input_numerical_sparse = csr_matrix(input_features_scaled)
    input_combined = hstack([input_ingredients_transformed, input_numerical_sparse])

    distances, indices = knn.kneighbors(input_combined)

    recommendations = recipe_df.iloc[indices[0]]
    return recommendations[['recipe_name', 'ingredients_list', 'image_url']]

# Test
input_features = [15, 36, 1, 42, 21, 81, 2, 'pork belly, smoked paprika, kosher salt']
print(recommend_recipes(input_features))