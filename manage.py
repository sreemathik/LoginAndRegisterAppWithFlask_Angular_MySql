import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app.server import app, db
from app.server.models import User


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.add_command('runserver', Server(host='0.0.0.0'))
    manager.run()
