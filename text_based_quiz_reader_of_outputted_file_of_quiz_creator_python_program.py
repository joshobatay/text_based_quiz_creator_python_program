import json
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() 

file_path = filedialog.askopenfilename(
    title="Select a quiz file",
    filetypes=[("JSON files", "*.json"), ("Text files", "*.txt")]
)

# Testing sample code for reading a text-based quiz file
with open(file_path, "r", encoding="utf-8") as file:
    quiz_data = json.load(file)
    
    print(quiz_data)

