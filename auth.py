import hashlib
from db_manager import DBManager

class Auth:
    def __init__(self):
        self.db = DBManager()

    def sign_in(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = self.db.get_user(username, hashed_password)
        if user:
            return user
        else:
            print("Invalid login credentials")
            return None

    def sign_up(self, username, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.db.insert_user(username, email, hashed_password)
        print("Sign-up successful")
