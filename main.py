import os
from database.db_handler import DBHandler
from recipe_api.recipe_api_handler import RecipeAPIHandler


def main():
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        print("Please set the SPOONACULAR_API_KEY environment variable.")
        return

    db_handler = DBHandler("ingredients.db")
    recipe_handler = RecipeAPIHandler(api_key)


if __name__ == "__main__":
    main()
