import os, sys
import importlib
import pkgutil


# импортируем все модели в файл, чтобы они были доступны при импорте from .models import ...
for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
	imported_module = importlib.import_module('.' + name, package='app.models')
	class_name = list(filter(lambda x: not x.startswith('__'), dir(imported_module)))[0]
	model_class = getattr(imported_module, class_name)
	setattr(sys.modules[__name__], name, model_class)
