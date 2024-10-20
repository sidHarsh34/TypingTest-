from db_manager import DBManager
from tkinter import messagebox

class Auth:
    def __init__(self):
        self.db = DBManager()

    def sign_in(self, username, password):
        user = self.db.get_user(username, password)
        if user:
            messagebox.showinfo("Login Success", f"Welcome back {username}!")
            return user
        else:
            messagebox.showerror("Login Error", "Invalid username or password.")
            return None

    def sign_up(self, username, email, password):
        if self.db.add_user(username, email, password):
            messagebox.showinfo("Sign Up Success", "Account created successfully! Please log in.")
        else:
            messagebox.showerror("Sign Up Error", "Username already exists.")
