#!/usr/bin/python3
"""Write a Python script that,
using this https://jsonplaceholder.typicode.com/,
for a given employee ID, returns information
about his/her TODO list progress.
"""
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
    list_tasks_done = []
    for task in tasks:
        if task.get('completed'):
            list_tasks_done.append(task.get("title"))

    NUMBER_OF_DONE_TASKS = len(list_tasks_done)
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    m = "Employee {} is done with tasks({}/{}):"
    print(m.format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for l in list_tasks_done:
        print("\t {}".format(l))
