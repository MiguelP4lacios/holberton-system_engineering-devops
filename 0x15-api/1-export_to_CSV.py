#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    employee_id = int(argv[1])
    URL_EMPLOYEE = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    URL_TASKS = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    employee = requests.get(URL_EMPLOYEE).json()
    tasks = requests.get(URL_TASKS).json()

    EMPLOYEE_NAME = employee.get('name')

    with open("{}.csv".format(employee_id), mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [argv[1], EMPLOYEE_NAME, task.get(
                'completed'), task.get('title')]
            writer.writerow(row)
