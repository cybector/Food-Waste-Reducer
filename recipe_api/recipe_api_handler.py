import requests


class RecipeAPIHandler:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_recipes(self, ingredients):
        # Create a comma-separated list of ingredients
        ingredient_list = ",".join([ingredient[0] for ingredient in ingredients])

        # Make a request to the API
        response = requests.get(
            f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient_list}&apiKey={self.api_key}"
        )

        # If the request failed, print the status code and return an empty list
        if response.status_code != 200:
            print(f"Failed to fetch recipes: {response.status_code}")
            return []

        # Return the list of recipes
        recipes = response.json()
        return recipes
