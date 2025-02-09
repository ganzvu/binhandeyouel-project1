import random

questions = [
    {"question": "5 + 7?", "options": ["A) 10", "B) 11", "C) 12", "D) 13"], "answer": "C"},
    {"question": "What is the square root of 64?", "options": ["A) 6", "B) 7", "C) 8", "D) 9"], "answer": "C"},
    {"question": "9 x 9?", "options": ["A) 72", "B) 81", "C) 99", "D) 90"], "answer": "B"},
    {"question": "100/4?", "options": ["A) 20", "B) 25", "C) 30", "D) 40"], "answer": "B"},
    {"question": "15% of 200?", "options": ["A) 25", "B) 30", "C) 35", "D) 40"], "answer": "B"}
]

def get_random_question():
    return random.choice(questions)
