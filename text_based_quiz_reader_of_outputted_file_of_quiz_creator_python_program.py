import json
import tkinter as tk
from tkinter import filedialog

# Main Menu
def main_menu():
    print("Welcome to the Quiz Reader!")
    print("1. Read a quiz file")
    print("2. Developer Information")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        quiz_reader()
    elif choice == "2":
        developer_info()
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Main function to run the program
def quiz_reader():
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(
        title="Select a quiz file",
        filetypes=[("JSON files", "*.json"), ("Text files", "*.txt")]
    )

    with open(file_path, "r", encoding="utf-8") as file:
        quiz_data = json.load(file)
        
        print(quiz_data)

# Developer information
def developer_info():
    print("Developer: BSCpE 1-6 | Gabriel Josh A. Obatay")
    print("Email: joshobatay2005@gmail.com")

main_menu()

