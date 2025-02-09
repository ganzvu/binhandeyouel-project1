import random

questions = [
    {"question": "What is the chemical symbol for gold?", "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"], "answer": "A"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"], "answer": "B"},
    {"question": "What is the powerhouse of the cell?", "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Golgi apparatus"], "answer": "C"},
    {"question": "What gas do plants primarily take in for photosynthesis?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"], "answer": "B"},
    {"question": "What is H2O commonly known as?", "options": ["A) Oxygen", "B) Water", "C) Hydrogen", "D) Salt"], "answer": "B"}
]

def get_random_question():
    return random.choice(questions)
