#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    task_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    task_json = get(task_url).json()
    name_json = get(name_url).json()

    task_num = len(task_json)
    task_complete = len([task for task in task_json
                         if task.get("completed")])
    name = name_json.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, task_complete, task_num))
    for task in task_json:
        if (task.get("completed")):
            print("\t {}".format(task.get("title")))
