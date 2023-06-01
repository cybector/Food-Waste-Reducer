import requests


class RecipeAPIHandler:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_recipes(self, ingredients):
        ingredient_list = ",".join([ingredient[0] for ingredient in ingredients])

        response = requests.get(
            f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient_list}&apiKey={self.api_key}"
        )

        if response.status_code != 200:
            print(f"Failed to fetch recipes: {response.status_code}")
            return []

        recipes = response.json()
        return recipes
