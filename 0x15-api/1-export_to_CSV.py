#!/usr/bin/python3
""" Script to export data in the CSV format. """
import csv
import requests as r
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = r.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    to_do = r.get(url + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]
