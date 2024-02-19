#!/usr/bin/python3
# Gathers to-do list info for a given employee ID and exports to CSV
import csv
import requests
from sys import argv


if __name__ == "__main__":
    '''Gives employee ID info and exports as CSV'''
    if len(argv) is not 2:
        print("Command takes 2 arguments")
        exit
    _id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    req = requests.get(url)
    jreq = req.json()
    name = jreq['username']
    url = "https://jsonplaceholder.typicode.com/todos"
    req = requests.get(url)
    jreq = req.json()
    tasks = []
    tasks_dict = []
    for i in jreq:
        if i['userId'] == int(_id):
            tasks.append(i)
    for i in tasks:
        tasks_dict.append({'name': name,
                           'id': _id,
                           'completed': i['completed'],
                           'title': i['title']})
    with open('{}.csv'.format(_id), mode='w') as csv_file:
        fieldnames = ['id', 'name', 'completed', 'title']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for i in tasks_dict:
            writer.writerow(i)
