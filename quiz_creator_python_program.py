# Quiz Creator Python Program 

from colorama import Fore # Module for colored text
import pyfiglet # Module for ASCII art
import json # Module for JSON handling

# Front page of the program
def front_page():
    text = pyfiglet.figlet_format(text = "Welcome to the Quiz Creator!", font = "ansi_regular", width = 150) # Create ASCII art for the welcome message
    print(Fore.CYAN + text + Fore.RESET) # Print the welcome message in cyan color, reset color after

    # Main menu of the program
    print("""
        1. Create your own quiz
        2. Meet the developer
        3. Exit the program
        """)
    user_choice = input("Enter your choice: ").strip().lower() # Get user input for the choice
    if user_choice in ["1", "one", "Create your own quiz"]:
        quiz_creator()
       


def quiz_creator():
    quiz_question = {
        
    }

    destination = "C:/Users/josho/OneDrive/Desktop/output.json"

    try:
        with open(destination, "w") as file:
            json.dump(quiz_question, file, indent = 4)
            print("JSON file created successfully.")
    except FileExistsError:
        print("File already exists")



front_page()