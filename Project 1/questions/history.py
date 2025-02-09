import random

questions = [
    {"question": "Who was the first President of the United States?", "options": ["A) Abraham Lincoln", "B) George Washington", "C) Thomas Jefferson", "D) John Adams"], "answer": "B"},
    {"question": "Which year did World War II end?", "options": ["A) 1941", "B) 1945", "C) 1939", "D) 1950"], "answer": "B"},
    {"question": "Who discovered America in 1492?", "options": ["A) Christopher Columbus", "B) Marco Polo", "C) Vasco da Gama", "D) Ferdinand Magellan"], "answer": "A"},
    {"question": "Which civilization built the pyramids?", "options": ["A) Romans", "B) Greeks", "C) Egyptians", "D) Persians"], "answer": "C"},
    {"question": "What was the name of the ship that brought the Pilgrims to America?", "options": ["A) Santa Maria", "B) Mayflower", "C) Titanic", "D) Queen Mary"], "answer": "B"}
]

def get_random_question():
    return random.choice(questions)
