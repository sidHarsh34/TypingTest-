from tkinter import *
from tkinter import messagebox
from auth import Auth
from typing_test import TypingTest
import random
import time

class TypingTestUI:
    def __init__(self):
        self.auth = Auth()
        self.root = Tk()
        self.root.title("MonkeyType - Typing Test")
        self.root.geometry("800x500")
        self.root.config(bg="#121212")

        # Initial layout: Sign In page
        self.create_sign_in_ui()

        self.root.mainloop()

    def create_sign_in_ui(self):
        """Create the Sign In UI layout."""
        self.clear_ui()

        self.label = Label(self.root, text="Sign In", font=("Arial", 24, "bold"), bg="#121212", fg="white")
        self.label.pack(pady=20)

        self.username_label = Label(self.root, text="Username", font=("Arial", 12), bg="#121212", fg="white")
        self.username_label.pack()
        self.username_entry = Entry(self.root, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        self.password_label = Label(self.root, text="Password", font=("Arial", 12), bg="#121212", fg="white")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=5)

        self.sign_in_button = Button(self.root, text="Sign In", command=self.sign_in, width=20, bg="#007acc", fg="white", font=("Arial", 12, "bold"))
        self.sign_in_button.pack(pady=20)

        self.toggle_to_sign_up = Button(self.root, text="Don't have an account? Sign Up", command=self.create_sign_up_ui, bg="#121212", fg="#007acc", font=("Arial", 10, "italic"), bd=0)
        self.toggle_to_sign_up.pack(pady=10)

    def create_sign_up_ui(self):
        """Create the Sign Up UI layout."""
        self.clear_ui()

        self.label = Label(self.root, text="Sign Up", font=("Arial", 24, "bold"), bg="#121212", fg="white")
        self.label.pack(pady=20)

        self.username_label = Label(self.root, text="Username", font=("Arial", 12), bg="#121212", fg="white")
        self.username_label.pack()
        self.username_entry = Entry(self.root, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        self.email_label = Label(self.root, text="Email", font=("Arial", 12), bg="#121212", fg="white")
        self.email_label.pack()
        self.email_entry = Entry(self.root, width=30, font=("Arial", 12))
        self.email_entry.pack(pady=5)

        self.password_label = Label(self.root, text="Password", font=("Arial", 12), bg="#121212", fg="white")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=5)

        self.sign_up_button = Button(self.root, text="Sign Up", command=self.sign_up, width=20, bg="#007acc", fg="white", font=("Arial", 12, "bold"))
        self.sign_up_button.pack(pady=20)

        self.toggle_to_sign_in = Button(self.root, text="Already have an account? Sign In", command=self.create_sign_in_ui, bg="#121212", fg="#007acc", font=("Arial", 10, "italic"), bd=0)
        self.toggle_to_sign_in.pack(pady=10)

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.auth.sign_in(username, password)
        if user:
            self.show_typing_test(username)

    def sign_up(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.auth.sign_up(username, email, password)

    def clear_ui(self):
        """Clear the current UI widgets before switching forms."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_typing_test(self, username):
        """Display the main typing test UI after a successful login."""
        self.clear_ui()

        self.label = Label(self.root, text=f"Welcome, {username}! Select Typing Mode:", font=("Arial", 18, "bold"), bg="#121212", fg="white")
        self.label.pack(pady=20)

        self.mode_choice = IntVar(value=1)  # 1 for words, 2 for paragraph
        self.words_radio = Radiobutton(self.root, text="Words", variable=self.mode_choice, value=1, font=("Arial", 12), bg="#121212", fg="white", selectcolor="#121212")
        self.words_radio.pack(pady=5)
        self.paragraph_radio = Radiobutton(self.root, text="Paragraph", variable=self.mode_choice, value=2, font=("Arial", 12), bg="#121212", fg="white", selectcolor="#121212")
        self.paragraph_radio.pack(pady=5)

        self.label_difficulty = Label(self.root, text="Select Difficulty Level:", font=("Arial", 14, "bold"), bg="#121212", fg="white")
        self.label_difficulty.pack(pady=10)

        self.difficulty_choice = IntVar(value=1)  # 1 for easy, 2 for medium, 3 for hard
        self.easy_radio = Radiobutton(self.root, text="Easy", variable=self.difficulty_choice, value=1, font=("Arial", 12), bg="#121212", fg="white", selectcolor="#121212")
        self.easy_radio.pack(pady=5)
        self.medium_radio = Radiobutton(self.root, text="Medium", variable=self.difficulty_choice, value=2, font=("Arial", 12), bg="#121212", fg="white", selectcolor="#121212")
        self.medium_radio.pack(pady=5)
        self.hard_radio = Radiobutton(self.root, text="Hard", variable=self.difficulty_choice, value=3, font=("Arial", 12), bg="#121212", fg="white", selectcolor="#121212")
        self.hard_radio.pack(pady=5)

        self.start_button = Button(self.root, text="Start Test", command=self.start_typing_test, width=20, bg="#28a745", fg="white", font=("Arial", 12, "bold"))
        self.start_button.pack(pady=20)

    def start_typing_test(self):
        """Start the typing test based on the selected mode and difficulty."""
        mode = self.mode_choice.get()
        difficulty = self.difficulty_choice.get()

        self.clear_ui()
        self.start_time = time.time()  # Start time tracking

        self.test = TypingTest()
        if mode == 1:  # Words mode
            self.text_to_type = self.test.get_words(difficulty)
        else:  # Paragraph mode
            self.text_to_type = self.test.get_paragraph(difficulty)

        self.display_text = Label(self.root, text=self.text_to_type, font=("Arial", 14, "italic"), bg="#ffffff", fg="#333", padx=10, pady=10, wraplength=600)
        self.display_text.pack(pady=10)

        self.typing_entry = Entry(self.root, width=50, font=("Arial", 12))
        self.typing_entry.pack(pady=10)
        self.typing_entry.bind("<KeyRelease>", self.check_completion)

    def check_completion(self, event):
        """Automatically submit the test when all the text is typed."""
        typed_text = self.typing_entry.get()
        if typed_text.strip() == self.text_to_type.strip():
            self.submit_typing_test()

    def submit_typing_test(self):
        """Calculate and display WPM, accuracy, and score after test submission."""
        typed_text = self.typing_entry.get()
        end_time = time.time()

        if typed_text:
            time_taken = end_time - self.start_time
            wpm, accuracy, score = self.test.calculate_metrics(typed_text, self.text_to_type, time_taken)
            self.show_result_page(wpm, accuracy, score)
        else:
            messagebox.showerror("Error", "Please type the text before submitting.")

    def show_result_page(self, wpm, accuracy, score):
        """Show the result on a separate page with better styling."""
        self.clear_ui()

        self.result_label = Label(self.root, text="Typing Test Results", font=("Arial", 24, "bold"), bg="#121212", fg="white")
        self.result_label.pack(pady=20)

        result_text = f"""
        Words Per Minute (WPM): {wpm:.2f}
        Accuracy: {accuracy:.2f}%
        Final Score: {score:.2f}
        """
        self.result_display = Label(self.root, text=result_text, font=("Arial", 16), bg="#121212", fg="white")
        self.result_display.pack(pady=10)

        self.restart_button = Button(self.root, text="Try Again", command=self.show_typing_test, width=20, bg="#007acc", fg="white", font=("Arial", 12, "bold"))
        self.restart_button.pack(pady=20)
