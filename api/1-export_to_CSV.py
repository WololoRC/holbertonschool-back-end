#!/usr/bin/python3
"""Gather data from JSONPlacehole with input"""
import requests
from sys import argv


a_out = []
a_state = []

r_name = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(argv[1]))
r_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

for record in r_todos.json():
    a_out.append(record.get('title'))
    a_state.append(record.get('completed'))

u = r_name.json()[0].get('username')

with open(f"{argv[1]}.CSV", 'w', encoding="utf-8") as a_file:
    for done in zip(a_out, a_state):
        a_file.write(
                '"{}","{}","{}","{}"\n'.format(argv[1], u, done[1], done[0]))
