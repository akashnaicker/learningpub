import json

# Open and read the JSON file
with open('object.json', 'r') as file:
    data = json.load(file)

# Accessing data from the JSON file
print(data['name'])       # Output: John Doe
print(data['age'])        # Output: 30
print(data['isStudent'])  # Output: False
print(data['address']['city'])  # Output: Anytown
print(data['hobbies'])    # Output: ['reading', 'gaming', 'coding']
print(data)    