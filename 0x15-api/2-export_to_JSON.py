#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

from requests import get
from sys import argv
from json import dump

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    task_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    task_json = get(task_url).json()
    name_json = get(name_url).json()

    task_list = []
    for task in task_json:
        task_dict = {}
        task_dict.update({"user_ID": argv[1], "username": name_json.get(
            "username"), "completed": task.get("completed"),
                          "task": task.get("title")})
        task_list.append(task_dict)
    
    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: task_list}, f)
