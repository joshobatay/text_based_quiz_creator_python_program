# Quiz Creator Python Program 

from colorama import Fore # Module for colored text
from pathlib import Path # Module for file path handling
import os # Module for operating system functions
import pyfiglet # Module for ASCII art
import json # Module for JSON handling

# Front page of the program
def main_menu():
    while True:
        text = pyfiglet.figlet_format(text = "Welcome to the Quiz Creator!", font = "ansi_regular", width = 150) # Create ASCII art for the welcome message
        print(Fore.CYAN + text + Fore.RESET) # Print the welcome message in cyan color, reset color after

        # Main menu of the program
        print("""
1. Create your own quiz
2. Meet the developer
3. Exit the program
            """)
        user_choice = input("Enter your choice: ").strip().lower() # Get user input for the choice
        if user_choice in ["1", "one", "create your own quiz"]:
            quiz_creator()
        elif user_choice in ["2", "two", "meet the developer"]:
            developer_info()
        elif user_choice in ["3", "three", "exit the program"]:
            clear_screen()
            print("Exiting the program...")
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")
            
# Ask user if they want to add more questions, program will stop and return to main menu if they say no
# Save the quiz in JSON format             
            
def quiz_creator():
    clear_screen()
    
    # Ask user for name of the quiz
    quiz_name = input("Enter the name of the quiz: ").strip() # Ask user for the name of the quiz
    
    quiz_data = {
        "quiz_name": quiz_name, # Stores the entered quiz name
        "questions": {} # Dictionary to store entered questions and correct answers
    }
    
    while True:
        
        question = input("Enter a question: ").strip() # Asks the user for a question
        
        print(Fore.YELLOW + "Enter the Choices:" + Fore.RESET)
        choice_A = input("A: ").strip() # First choice
        choice_B = input("B: ").strip() # Second choice
        choice_C = input("C: ").strip() # Third choice
        choice_D = input("D: ").strip() # Fourth choice
        
        correct_answer = input("Enter the correct answer A|B|C|D: ").strip().upper() # Ask user for the correct answer
        explanation = input("Enter the explanation: ").strip() # Ask user for the explanation of the correct answer
        

        quiz_question = {
            "Question": question,
            "Choices": {
                "A": choice_A,
                "B": choice_B,
                "C": choice_C,
                "D": choice_D
                
            },
            "Correct Answer": correct_answer,
            "Explanation": explanation,
            
        }
        
        quiz_data["questions"][question] = quiz_question

        desktop_path = Path.home() / "Desktop" # Path of the user's Desktop
        destination = desktop_path / "create_your_own_quiz.json" # Destination for the JSON file

        try:
            with open(destination, "w") as file:
                json.dump(quiz_question, file, indent = 4)
                print("JSON file created successfully.")
        except FileExistsError:
            print("File already exists")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen for Windows or Unix-based systems
    
def developer_info():
    while True:
        clear_screen()
        print(Fore.GREEN + """
Program made by: BSCpE 1-6 | Gabriel Josh A. Obatay
    """ + Fore.RESET) # Print developer information in green color, reset color after
        choice = input("Press 'b' to go back to the main menu: ").strip().lower() 
        if choice == "b":
            clear_screen()
            break
        
main_menu()