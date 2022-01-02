import argparse
import itertools
import sqlite3
from concurrent.futures import ProcessPoolExecutor

import requests as requests
from decouple import config

conn = sqlite3.connect(config("SEED_DB_URI"))
URL = "https://api.github.com/users?per_page={per_page}&page={page}"


class UserModel:
    def __init__(self):
        self.cursor = conn.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS github_users (_id INTEGER PRIMARY KEY,
                id INTEGER, username VARCHAR(150), avatar_url VARCHAR(150), type VARCHAR(150), URL TEXT)""")

    def insert(self, data):
        query = self.cursor.executemany(
            "INSERT INTO github_users (id, username, avatar_url, type, URL) VALUES (?, ?, ?, ?, ?);", data)
        conn.commit()


def fetch_github_users_in_parallel(total_users, break_by):
    partition = partition_no(total_users, break_by)
    with ProcessPoolExecutor() as pool:
        result = pool.map(fetch_github_users, partition)
    return list(itertools.chain(*result))


def fetch_github_users(partition):
    """Fetch users from GitHub

    Parameters:
    partition (tuple): A tuple of "number of query per page"  and page number e.g (100, 1)

    Returns:
    array: Returning a list of users dicts
    """
    per_page, page = partition[0], partition[1]
    url = URL.format(per_page=per_page, page=page)
    try:
        req = requests.get(url)
        return [(x.get("id"), x.get("login"), x.get("avatar_url"), x.get("type"), x.get("url")) for x in req.json()]
    except Exception as e:
        print("Error connection to {}".format(url))
        return None


def partition_no(number, break_by):
    users = []
    page = 0
    while number > break_by:
        page += 1
        number -= break_by
        users.append((break_by, page))
    if number:
        users.append((number, page + 1))
    return users


def main():
    db = UserModel()  # Initialize Database
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--total', help="Number of users to get from GitHub", type=int)
    args = parser.parse_args()

    total_users = args.total if args.total else 150
    if total_users > 100:
        users_json = fetch_github_users_in_parallel(total_users, 100)
    else:
        users_json = fetch_github_users((total_users, 1))

    if users_json:
        print("Inserting into database .....")
        db.insert(users_json)
        print("Done Inserting into database .....")


if __name__ == "__main__":
    main()
