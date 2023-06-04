import requests


class RecipeAPIHandler:
    def __init__(self, api_key):
        self.api_key = api_key  # Store the API key

    def fetch_recipes(self, ingredients):
        # Create a comma-separated list of ingredients
        ingredient_list = ",".join([ingredient[0] for ingredient in ingredients])

        # API endpoint
        api_endpoint = "https://api.spoonacular.com/recipes/findByIngredients"

        # Prepare URL for the API request
        url = f"{api_endpoint}?ingredients={ingredient_list}&apiKey={self.api_key}"

        # Make a request to the API with a 5-second timeout
        response = requests.get(url, timeout=5)

        # If the request failed, print the status code and return an empty list
        if response.status_code != 200:
            print(f"Failed to fetch recipes: {response.status_code}")
            return []

        # Parse the JSON response and return the list of recipes
        recipes = response.json()
        return recipes
