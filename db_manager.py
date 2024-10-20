import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("db/typing_test.db")
        self.create_users_table()

    def create_users_table(self):
        """Create the users table if it does not exist."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                );
            """)

    def insert_user(self, username, email, password):
        """Insert a new user into the users table."""
        with self.conn:
            self.conn.execute("""
                INSERT INTO users (username, email, password) VALUES (?, ?, ?)
            """, (username, email, password))

    def get_user(self, username, password):
        """Retrieve a user from the database based on username and password."""
        with self.conn:
            user = self.conn.execute("""
                SELECT * FROM users WHERE username = ? AND password = ?
            """, (username, password)).fetchone()
        return user
