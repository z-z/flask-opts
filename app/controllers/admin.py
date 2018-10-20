from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from app import db
from app.models import Category
from app.models import Product


bp = Blueprint(__name__, __name__, url_prefix='/admin')


@bp.route('/')
def index():
	categories = Category.query.all()
	products = Product.query.all()
	return render_template('admin/index.html', categories=categories, products=products)


@bp.route('/add/category', methods=['GET', 'POST'])
def add_category():

	name = request.form.get('name')
	parent_id = request.form.get('parent_id')

	category = Category()
	category.name = name

	if parent_id is not None:
		parent = Category.query.get(parent_id)
		if parent is not None:
			category.parent = parent

	db.session.add(category)
	db.session.commit()

	return redirect('/admin/', code=302)


@bp.route('/add/product', methods=['GET', 'POST'])
def add_product():

	name = request.form.get('name')
	category_id = request.form.get('category_id')

	product = Product()
	product.name = name
	product.category = Category.query.get(category_id)

	db.session.add(product)
	db.session.commit()

	return redirect('/admin/', code=302)