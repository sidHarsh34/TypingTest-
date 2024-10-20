import random
from db_manager import DBManager

class TypingTest:
    def __init__(self, user_id):
        self.db = DBManager()
        self.user_id = user_id
        self.words = ["python", "development", "computer", "programming", "interface", "keyboard", "screen"]
        self.paragraphs = [
            "Python is a high-level programming language.", 
            "It supports multiple programming paradigms."
        ]

    def start_word_test(self):
        random.shuffle(self.words)
        # The game logic for word-based test will go here
        # For simplicity, let's say the score is calculated
        score = 5
        accuracy = 98.5
        self.update_score(score, accuracy)

    def start_paragraph_test(self):
        random.shuffle(self.paragraphs)
        # The game logic for paragraph-based test will go here
        # For simplicity, let's say the score is calculated
        score = 10
        accuracy = 95.2
        self.update_score(score, accuracy)

    def update_score(self, score, accuracy):
        self.db.update_score(self.user_id, score, accuracy)
