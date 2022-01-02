import argparse
import itertools
import os
from concurrent.futures import ProcessPoolExecutor
import requests as requests

from sqlalchemy import create_engine


URL = "https://api.github.com/users?per_page={per_page}&page={page}"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'app/main/database/github_users.db')

engine = create_engine("sqlite:///" + DATABASE_PATH)
conn = engine.connect()


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
        conn.execute(
            "INSERT INTO github_users (id, username, avatar_url, type, URL) VALUES (?, ?, ?, ?, ?);",
            users_json
        )
        print("Done Inserting into database .....")


if __name__ == "__main__":
    main()
