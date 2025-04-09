# Quiz Creator Python Program 

from colorama import Fore # Module for colored text
from pathlib import Path # Module for file path handling
import os # Module for operating system functions
import pyfiglet # Module for ASCII art
import json # Module for JSON handling

# Front page of the program
def main_menu():
    while True:
        text = pyfiglet.figlet_format(text = "Welcome to the Quiz Creator!", 
                                      font = "ansi_regular", 
                                      width = 150
                                      ) # Create ASCII art for the welcome message
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
                        
def quiz_creator():
    clear_screen()
    
    # Ask user for name of the quiz
    quiz_name = input(Fore.YELLOW + "Enter the name of the quiz: "+ Fore.RESET
                      ).strip() # Ask user for the name of the quiz
    
    quiz_data = {
        "quiz_name": quiz_name, # Stores the entered quiz name
        "questions": {} # Dictionary to store entered questions and correct answers
    }
    
    question_count = 1
    
    while True:
       # clear_screen()
        question = input(Fore.YELLOW + f"Enter question {question_count}: " + Fore.RESET
                         ).strip() # Asks the user for a question
        
        print(Fore.YELLOW + "Enter the Choices:" + Fore.RESET)
        choice_A = input(Fore.YELLOW + "A: " + Fore.RESET).strip() # First choice
        choice_B = input(Fore.YELLOW + "B: " + Fore.RESET).strip() # Second choice
        choice_C = input(Fore.YELLOW + "C: " + Fore.RESET).strip() # Third choice
        choice_D = input(Fore.YELLOW + "D: " + Fore.RESET).strip() # Fourth choice
        
        while True:
            correct_answer = input(Fore.YELLOW + "Enter the correct answer (A|B|C|D): " + Fore.RESET
                                ).strip().upper() # Ask user for the correct answer
            if correct_answer in ["A", "B", "C", "D"]:
                break
            else:
                print(Fore.RED + "Invalid choice. Please enter A, B, C, or D." + Fore.RESET)

        explanation = input(Fore.YELLOW + "Enter the explanation: " + Fore.RESET
                            ).strip() # Ask user for the explanation of the correct answer
        
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
        
        question_name = f"quiz_question{question_count}"
        quiz_data["questions"][question_name] = quiz_question
        
        clear_screen()
        print(f"Quiz name: {Fore.GREEN + quiz_name + Fore.RESET}")
        print(f"Added Question: {Fore.GREEN + question + Fore.RESET}")
        print(f"A: {Fore.GREEN + choice_A + Fore.RESET}\nB: {Fore.GREEN + choice_B + Fore.RESET}")
        print(f"C: {Fore.GREEN + choice_C + Fore.RESET}\nD: {Fore.GREEN + choice_D + Fore.RESET}" )
        print(f"Correct Answer: {Fore.GREEN + correct_answer + Fore.RESET}")
        print(f"Explanation: {Fore.GREEN + explanation + Fore.RESET}")
        
        # Ask user if they want to add more questions, program will stop and return to main menu if they type stop
        continue_choice = input(
            f"Do you want to create another question? "
            f"(Type {Fore.RED + 'stop' + Fore.RESET} to quit or press Enter to continue): ").strip().lower()
        if continue_choice == "stop":
            clear_screen()
            print(Fore.MAGENTA + "Exiting the quiz creator..." + Fore.RESET)
            break
    
        question_count += 1
        clear_screen()
    
    if quiz_data["questions"]:    
        desktop_path = Path.home() / "Desktop" # Path of the user's Desktop
        destination = desktop_path / "create_your_own_quiz.json" # Destination for the JSON file

    if os.path.exists(destination):
        overwrite = input(
            f"The file '{destination}' {Fore.RED + 'already exists.' + Fore.RESET} "
            f"Do you want to {Fore.RED + 'overwrite it?' + Fore.RESET} (yes/no): ").strip().lower()
        clear_screen()
        if overwrite == "yes":
            try:
                # Save the quiz in JSON format  
                with open(destination, "w") as file:
                    json.dump(quiz_data, file, indent = 4)
                    print("JSON file created successfully.")
            except Exception as e:
                print(f"An error occured: {e}")
        else:
            print(Fore.MAGENTA + "File not overwritten." + Fore.RESET)
    
    else:
        try:
            with open(destination, "w") as file:
                json.dump(quiz_data, file, indent=4)
                print("JSON file created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

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
