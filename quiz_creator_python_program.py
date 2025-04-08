# Quiz Creator Python Program 

from colorama import Fore # Module for colored text
import pyfiglet # Module for ASCII art
import json # Module for JSON handling


text = pyfiglet.figlet_format(text = "Welcome to the Quiz Creator!", font = "ansi_regular", width = 100)
print(Fore.CYAN + text)


'''

quiz_question = {
    
}

destination = "C:/Users/josho/OneDrive/Desktop/output.json"

try:
    with open(destination, "w") as file:
        json.dump(quiz_question, file, indent = 4)
        print("JSON file created successfully.")
except FileExistsError:
    print("File already exists")

'''
