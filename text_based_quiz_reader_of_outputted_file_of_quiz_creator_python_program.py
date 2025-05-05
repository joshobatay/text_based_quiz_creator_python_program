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
    
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(
        title="Select a quiz file",
        file_types=[("JSON files", "*.json"), ("Text files", "*.txt")]
    )

    with open(file_path, "r", encoding="utf-8") as file:
        quiz_data = json.load(file)
        
        print(quiz_data)

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

