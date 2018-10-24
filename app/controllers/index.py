from flask import Blueprint
from flask import render_template
from flask import request
from app.models import Category
from app.models import Product


bp = Blueprint(__name__, __name__, url_prefix='/')


@bp.route('/')
def index():
	categories = Category.query.all()
	products = Product.query

	category = request.args.get('category', default = None, type = int)

	if category is not None:
		products = products.filter(Product.category_id.like(category))

	products = products.all()
	return render_template('index.html', categories=categories, products=products)
