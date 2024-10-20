import sqlite3
import os

class DBManager:
    def __init__(self):
        # Get the absolute path to the 'db' folder
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current file's directory
        db_dir = os.path.join(base_dir, 'db')

        # Ensure the 'db' directory exists
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        # Set the absolute path to the database file
        db_path = os.path.join(db_dir, 'typing_test.db')

        # Connect to the database
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create users table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                score INTEGER DEFAULT 0,
                accuracy REAL DEFAULT 0.0
            )
        ''')
        self.connection.commit()

    def add_user(self, username, email, password):
        try:
            self.cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                                (username, email, password))
            self.connection.commit()
        except sqlite3.IntegrityError:
            return False
        return True

    def get_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", 
                            (username, password))
        return self.cursor.fetchone()

    def update_score(self, user_id, score, accuracy):
        self.cursor.execute("UPDATE users SET score = ?, accuracy = ? WHERE id = ?", 
                            (score, accuracy, user_id))
        self.connection.commit()

    def close(self):
        self.connection.close()
