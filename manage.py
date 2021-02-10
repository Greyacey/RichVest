from gevent import monkey

monkey.patch_all()

from app.main.model.user import User
from uuid import uuid4

import os
import unittest

from dotenv import load_dotenv, find_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint

from app.main import create_app, db

load_dotenv(find_dotenv())

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def seed_admin():
    "Add seed data to the database."
    user = User(
        first_name='Grace',
        last_name='Ajibade',
        password='AdminUser55',
        email='admin@demo.com',
        public_id=uuid4()
    )
    db.session.add(user)
    db.session.commit()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
