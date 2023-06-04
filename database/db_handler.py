import sqlite3


class DBHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ingredients (
            name TEXT,
            expiry_date TEXT
            );
            """
        )

    def add_ingredient(self, name, expiry_date):
        self.cursor.execute(
            """
            INSERT INTO ingredients VALUES (?, ?);
            """,
            (name, expiry_date),  # Inserting provided ingredient into the database
        )
        self.conn.commit()

    def get_ingredients(self):
        self.cursor.execute(
            """
            SELECT * FROM ingredients;
            """
        )
        return self.cursor.fetchall()  # Fetching all ingredients from the database

    def close(self):
        self.conn.close()  # Closing the database connection
