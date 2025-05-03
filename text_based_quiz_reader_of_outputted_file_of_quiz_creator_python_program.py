import os
import json

filename = "create_your_own_quiz.json"
file_path = os.path.join(os.getcwd(), filename)

# Testing sample code for reading a text-based quiz file
with open(file_path, "r", encoding="utf-8") as file:
    quiz_data = json.load(file)

