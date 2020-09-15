#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    employee_id = int(argv[1])

    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)).json()

    with open('{}.csv'.format(employee_id), mode='w') as file:
        _writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            _writer.writerow([employee_id, employee.get('name'),
                              task.get('completed'), task.get('title')])
