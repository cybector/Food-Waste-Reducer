import os

from dotenv import load_dotenv

from database.db_handler import DBHandler
from recipe_api.recipe_api_handler import RecipeAPIHandler


def main():
    load_dotenv()
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        print(
            "Please set the SPOONACULAR_API_KEY environment variable in the .env file."
        )
        return

    db_handler = DBHandler("ingredients.db")
    recipe_handler = RecipeAPIHandler(api_key)

    db_handler.add_ingredient("Milk", "2023-06-10")
    db_handler.add_ingredient("Eggs", "2023-06-15")

    ingredients = db_handler.get_ingredients()

    recipes = recipe_handler.fetch_recipes(ingredients)
    print(recipes)

    db_handler.close()


if __name__ == "__main__":
    main()
