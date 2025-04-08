# Quiz Creator Python Program 

from colorama import Fore # Module for colored text
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
            
def quiz_creator():
    clear_screen()
    quiz_question = {
        
    }

    destination = "C:/Users/josho/OneDrive/Desktop/output.json"

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