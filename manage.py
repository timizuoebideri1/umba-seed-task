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
    app.run()


if __name__ == "__main__":
    manager.run()
