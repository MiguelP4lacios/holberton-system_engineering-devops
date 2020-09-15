#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    employee_id = argv[1]
    URL_EMPLOYEE = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    URL_TASKS = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    employee = requests.get(URL_EMPLOYEE).json()
    tasks = requests.get(URL_TASKS).json()

    data = {}
    data[employee_id] = []
    for task in tasks:
        data[employee_id.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee.get('name')
        })
    with open('{}.json'.format(employee_id), mode='w') as file:
        json.dump(data, file)
