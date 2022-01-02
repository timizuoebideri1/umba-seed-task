# UMBA GithHub Seed ReadMe

## Project SetUp
```sh
$ python3 -m venv env
$ source env/bin/active
$ pip install -r requirements.txt
$ cp env.example .env # make the proper configurations to the env variables
```
## Useful Commands
``` sh
$ python manage.py run # run project

# DATABASE COMMANDS
$ python manage.py db init # Initialize database
$ python manage.py db migrate # Generate migration version
$ python manage.py db upgrade # Upload changed to database
```

## Test
```sh
$ python manage.py test
```

## Seed GitHub Users to DB
```sh
$ python seed.py # seeds a total of 250
OR
$ python seed.py -t <no_to_seed>

```


