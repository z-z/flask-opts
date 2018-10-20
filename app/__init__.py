from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from . import controllers

application = Flask('app')
application.config['SECRET_KEY']                     = 'NjNBwf6>s>!qt6|7>gr@2Y{?EfroT<'
application.config['SQLALCHEMY_DATABASE_URI']        = 'mysql+pymysql://flasky:pass@word56@db4free.net/flasky'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.debug = True

db = SQLAlchemy(application)
migrate = Migrate(application, db)

controllers.init(application)

manager = Manager(application)
manager.add_command('db', MigrateCommand)
