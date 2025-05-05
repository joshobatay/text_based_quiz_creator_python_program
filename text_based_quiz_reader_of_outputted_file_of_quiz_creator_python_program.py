import os
import json
import tkinter as tk
from tkinter import filedialog

import pyfiglet
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama to reset colors automatically

# Main Menu
def main_menu():
    while True:
        text = "Welcome to the Quiz Reader!"
        print(Fore.YELLOW + pyfiglet.figlet_format(text,
                                                font="ansi_regular",
                                                width=100))
        print('''
1. Read a quiz file
2. Meet the developer
3. Exit the program
        ''')

        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            quiz_reader()
        elif user_choice == "2":
            developer_info()
        elif user_choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to run the program
def quiz_reader():
    
    clear_screen()
    
    temp_root = tk.Tk()
    temp_root.withdraw() 
    
    file_path = filedialog.askopenfilename(
        title="Select a quiz file",
        filetypes=[("JSON files", "*.json"), ("Text files", "*.txt")]
    )

    temp_root.destroy()  # Close the temporary root window

    if not file_path:
        print("No file selected. Returning to main menu.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            quiz_data = json.load(file)
            quiz_name = quiz_data["quiz_name"]
            questions = quiz_data["questions"]
            
            print(f"Welcome to the quiz: {quiz_name}\n")
        
            # Select difficulty level
            life_hearts = select_difficulty()
            score = 0
            
            for key, question_data in questions.items():
                print(f"\n{Fore.YELLOW}" + key.replace('_', ' ').title() + ": " + question_data['Question'])
                choices = question_data["Choices"]
                for option, answer in choices.items():
                    print(f"{option}: {answer}")

                # User input for answer
                user_answer = input("Your answer (A/B/C/D): ").strip().upper()

                # Check if the answer is correct
                if user_answer == question_data["Correct Answer"]:
                    score += 1
                    print(Fore.GREEN + "Correct!")
                else:
                    life_hearts -= 1
                    print(Fore.RED + f"Wrong! The correct answer was {question_data['Correct Answer']}.")
                    print(Fore.YELLOW + f"You have {life_hearts} life hearts left.")
                    
                while True:
                    print(f"Explanation: {question_data['Explanation']}\n")
                    input("Press any key to continue... ")
                    clear_screen()
                    break
            
                if life_hearts <= 0:
                    print(Fore.YELLOW + f"Score: {score} / {len(questions)}")
                    print(Fore.RED + "Game Over!")
                    break
            
        if life_hearts > 0:
            print(Fore.GREEN + f"Congratulations! You completed the quiz with a score of {score}/{len(questions)}.")
            
    except Exception as e:
        print(f"Error reading the file: {e}")
        
def select_difficulty():
    
    clear_screen()
    
    print(f'''
Select difficulty level:
{Fore.GREEN}1. Easy (10 lives)
{Fore.YELLOW}2. Medium (5 lives)
{Fore.RED}3. Hard (3 lives)
{Fore.MAGENTA}4. Hardcore (1 life)
''')

    difficuly_choice = input("Enter your choice (1 - 4): ")
    if difficuly_choice == "1":
        clear_screen()
        return 10
    elif difficuly_choice == "2":
        clear_screen()
        return 5
    elif difficuly_choice == "3":
        clear_screen()
        return 3
    elif difficuly_choice == "4":
        clear_screen()
        return 1
    else:
        clear_screen()
        print("Invalid choice. Defaulting to Easy difficulty.")
        return 10
    
# Developer information
def developer_info():
    
    clear_screen()
    
    while True:
        print(Fore.MAGENTA + "Developer: BSCpE 1-6 | Gabriel Josh A. Obatay")   
        print(Fore.GREEN + "Email: joshobatay2005@gmail.com")
        
        if input("Press 'b' to go back to the main menu: ").strip().lower() == "b":
            clear_screen()
            break
        else:
            print("Invalid input. Please try again.")
            clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
main_menu()

