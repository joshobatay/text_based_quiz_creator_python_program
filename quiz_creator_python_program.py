# Sample code testing

import json

cars = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 1983,
}

destination = "C:\Users\josho\OneDrive\Desktop\output.json"

try:
    with open(destination, "w") as file:
        json.dump(cars, file, indent = 4)
        print("JSON file created successfully.")
except FileExistsError:
    print("File already exists")
