import unittest

from decouple import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.main import config as umba_config, create_app, db

app = create_app(umba_config.configuration[config("UMBA_ENVIROMENT")])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def test():
    """Run unit tests."""
    tests = unittest.TestLoader().discover('app', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=1).run(tests)


if __name__ == "__main__":
    manager.run()
