import random

class TypingTest:
    easy_words = ["apple", "ball", "cat", "dog", "egg"]
    medium_words = ["keyboard", "monitor", "computer", "python", "table"]
    hard_words = ["pneumonia", "conscientious", "psychology", "supercalifragilisticexpialidocious"]

    easy_paragraph = "The cat is on the mat."
    medium_paragraph = "The quick brown fox jumps over the lazy dog."
    hard_paragraph = "Supercalifragilisticexpialidocious is a long and tricky word."

    def get_words(self, difficulty):
        if difficulty == 1:  # Easy
            return " ".join(random.choices(self.easy_words, k=5))
        elif difficulty == 2:  # Medium
            return " ".join(random.choices(self.medium_words, k=8))
        elif difficulty == 3:  # Hard
            return " ".join(random.choices(self.hard_words, k=10))

    def get_paragraph(self, difficulty):
        if difficulty == 1:  # Easy
            return self.easy_paragraph
        elif difficulty == 2:  # Medium
            return self.medium_paragraph
        elif difficulty == 3:  # Hard
            return self.hard_paragraph

    def calculate_metrics(self, typed_text, original_text, time_taken):
        word_count = len(original_text.split())
        wpm = (word_count / time_taken) * 60
        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(original_text) and c == original_text[i])
        accuracy = (correct_chars / len(original_text)) * 100
        score = wpm * (accuracy / 100)
        return wpm, accuracy, score
