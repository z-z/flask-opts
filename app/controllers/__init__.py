import os
import importlib


# инициализация всех контроллеров при запуске приложения
# есть проблема в том, что package указывается вручную
#
# в каждом контроллере необходимы две строки
#
# from flask import Blueprint
# bp = Blueprint('main', __name__, url_prefix='/')
#
# и далее декорировать экшены так: @bp.route('/')
#
def init(app):
    curr_path = os.path.dirname(os.path.abspath(__file__))
    files = (file[:-3] for file in os.listdir(curr_path) if file.endswith(".py") and file != '__init__.py')
    imported_modules = [importlib.import_module('.{}'.format(file), package='app.controllers') for file in files]
    for module in imported_modules:
        app.register_blueprint(getattr(module, 'bp'))
