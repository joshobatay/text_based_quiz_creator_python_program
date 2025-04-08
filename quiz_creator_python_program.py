# Sample code testing

import json

quiz_question = {
    "Question": "When was the Philippines discovered?",
    "Choices": {"A.": "1521", 
                "B.": "1777", 
                "C.": "1609", 
                "D.": "1236"
                },
    "Correct Answer": "A. 1521"
}

destination = "C:/Users/josho/OneDrive/Desktop/output.json"

try:
    with open(destination, "w") as file:
        json.dump(quiz_question, file, indent = 4)
        print("JSON file created successfully.")
except FileExistsError:
    print("File already exists")
