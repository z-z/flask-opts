from flask import Blueprint
from flask import render_template
from app.models import Category


bp = Blueprint(__name__, __name__, url_prefix='/')


@bp.route('/')
def index():
	categories = Category.query.all()
	return render_template('index.html', categories=categories)
