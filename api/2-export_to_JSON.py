#!/usr/bin/python3
"""
Gather data from JSONPlacehole with input
and export it ona JSON file.
"""
import requests
from sys import argv
import json

a_list = []
my_dict = {f"{argv[1]}": a_list}

r_name = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(argv[1]))
r_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

user = r_name.json()[0].get("username")

for r in r_todos.json():
    safe_dict = dict(
            task=r.get("title"), completed=r.get("completed"), username=user)

    a_list.append(safe_dict)

with open(f"{argv[1]}.json", 'w', encoding='utf-8') as a_json:
    json.dump(my_dict, a_json)
