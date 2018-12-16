from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from . import controllers

application = Flask('app')
application.config.from_object('app.config')

# если не будут удаляться элементы в БД
# SET FOREIGN_KEY_CHECKS = 0;

db = SQLAlchemy(application)
migrate = Migrate(application, db)

controllers.init(application)

manager = Manager(application)
manager.add_command('db', MigrateCommand)
