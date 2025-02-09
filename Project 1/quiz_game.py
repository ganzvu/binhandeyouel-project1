import random
import time
from questions import science, history, math
from colorama import Fore, Style, init

init(autoreset=True)

def display_welcome():
    print(Fore.CYAN + "Welcome to the Quiz Game!")
    print("You will be asked random questions from different categories.")
    print("Type A, B, C, or D to answer. Let's begin!\n")

def get_random_category():
    return random.choice([science, history, math])

def play_round():
    category = get_random_category()
    question_data = category.get_random_question()
    
    print(Fore.YELLOW + "Question: " + question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    user_answer = input(Fore.GREEN + "Your answer (A/B/C/D): ").strip().upper()

    if user_answer == question_data["answer"]:
        print(Fore.BLUE + "Correct!\n")
        return 1
    else:
        print(Fore.RED + f"Wrong! The correct answer was {question_data['answer']}.\n")
        return 0

def main():
    display_welcome()
    score = 0
    rounds = int(input("How many questions would you like to answer? "))

    for _ in range(rounds):
        score += play_round()
        time.sleep(1)

    print(Fore.MAGENTA + f"Game Over! Your final score: {score}/{rounds}")

if __name__ == "__main__":
    main()
