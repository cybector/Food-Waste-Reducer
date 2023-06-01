# database/db_handler.py

import sqlite3


class DBHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        """Create the ingredients table if it doesn't exist."""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ingredients (
                name TEXT,
                expiry_date TEXT
            );
        """
        )

    def add_ingredient(self, name, expiry_date):
        """Add an ingredient to the database."""
        self.cursor.execute(
            """
            INSERT INTO ingredients VALUES (?, ?);
        """,
            (name, expiry_date),
        )
        self.conn.commit()

    def get_ingredients(self):
        """Get all ingredients from the database."""
        self.cursor.execute(
            """
            SELECT * FROM ingredients;
        """
        )
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()
