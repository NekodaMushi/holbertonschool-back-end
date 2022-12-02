#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.


"""
# import json
import csv
import requests
from sys import argv

response_API = 'https://jsonplaceholder.typicode.com/'
if __name__ == "__main__":
    users = requests.get("{}users/{}".format(response_API, argv[1])).json()
    todos = requests.get("{}todos?userId={}".format(
        response_API, argv[1])).json()

    with open("{}.csv".format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todos:
            writer.writerow(["{}".format(argv[1]),
                             users['username'],
                             tasks['completed'],
                             tasks['title']])
