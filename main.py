import os
from dotenv import load_dotenv
from database.db_handler import DBHandler
from recipe_api.recipe_api_handler import RecipeAPIHandler


def main():
    load_dotenv()  # Load environment variables from .env file

    api_key = os.getenv(
        "SPOONACULAR_API_KEY"
    )  # Get Spoonacular API key from environment variable
    if not api_key:
        print(
            "Please set the SPOONACULAR_API_KEY environment variable in the .env file."
        )
        return

    db_handler = DBHandler("ingredients.db")  # Instantiate a database handler

    recipe_handler = RecipeAPIHandler(api_key)  # Instantiate a recipe API handler

    # Add ingredients to the database
    db_handler.add_ingredient("Milk", "2023-06-10")
    db_handler.add_ingredient("Eggs", "2023-06-15")

    ingredients = (
        db_handler.get_ingredients()
    )  # Fetch all ingredients from the database

    recipes = recipe_handler.fetch_recipes(
        ingredients
    )  # Fetch recipes based on the ingredients

    # Write the recipes to a text file
    with open("recipes.txt", "w", encoding="utf-8") as file:
        for recipe in recipes:
            file.write(str(recipe) + "\n")

    db_handler.close()  # Close the database connection


if __name__ == "__main__":
    main()  # Run the main function if the script is run directly
