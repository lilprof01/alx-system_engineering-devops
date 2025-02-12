#!/usr/bin/python3
"""
this script retrieves and save a user's TODO list in JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{user_id}"
    todos_url = f"{url}/todos?userId={user_id}"

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    username = user_response.get('username')
    tasks = []

    for task in todos_response:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    data = {user_id: tasks}
    filename = f"{user_id}.json"

    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
