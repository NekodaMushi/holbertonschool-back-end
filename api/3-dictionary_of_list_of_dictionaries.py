#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


response_API = 'https://jsonplaceholder.typicode.com/'

if __name__ == "__main__":
    res = requests.get("{}users".format(response_API)).json()
    # print(res)
    # tasks_list = [] scope problem !!
    tasks_dict = {}
    for user in res:
        name = user.get("username")
        # print(name)
        user_id = user.get("id")
        # print(user_id)
        tasks = requests.get("{}todos?userId={}".format(
            response_API, user_id)).json()
        # print(tasks)
        tasks_list = []
        # tasks_list moved, scope problem fixed
        for task in tasks:
            # print(task)
            t_d = {"username": name,
                   "task": task.get("title"),
                   "completed": task.get("completed")}
            tasks_list.append(t_d)
            # print(task)
        # print(user_id)
        tasks_dict[str(user_id)] = tasks_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)
