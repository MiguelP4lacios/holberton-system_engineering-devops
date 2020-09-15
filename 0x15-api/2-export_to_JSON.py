#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    USER_ID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        USER_ID)).json()
    list_to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            USER_ID)).json()

    dict_task = []
    for task in list_to_do:
        task_field = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')
        }
        dict_task.append(task_field)

    task_json = {}
    task_json[USER_ID] = dict_task
    with open('{}.json'.format(USER_ID), 'w') as file:
        json.dump(task_json, file)
