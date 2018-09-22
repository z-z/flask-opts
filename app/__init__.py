from flask import Flask
from flask_script import Manager

from . import controllers

application = Flask('app')
application.debug = True

controllers.init(application)

manager = Manager(application)
