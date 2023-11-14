import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')

# Get JSON encode string from rest api
todos = json.loads(response.text)
print(type(todos))
print(todos)

# Print only todos that are completed
for task in todos:
    if task['completed']:
        print(task)