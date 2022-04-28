from os import environ
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app
from models import db, Organization


app.config.from_object(environ.get('DELTA_ENV', 'config.Config'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()