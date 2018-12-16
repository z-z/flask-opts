import sys

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify

from app import db
from app.models import Category
from app.models import Product

from faker import Faker

from app.utils import get_random_elem


bp = Blueprint(__name__, __name__, url_prefix='/admin')


@bp.route('/')
def index():
	categories = Category.query.all()
	products = Product.query.all()
	return render_template('admin/index.html', categories=categories, products=products)

@bp.route('/faker')
def faker():
	if request.args.get('remove'):
		model = False
		if request.args.get('remove') == 'categories':
			model = Category
		if request.args.get('remove') == 'products':
			model = Product
		if model:
			model.query.delete()
			db.session.commit()

		return redirect('/admin/faker', code=302)

	if request.args.get('count') and request.args.get('model'):
		objs = []
		for i in range(int(request.args.get('count'))):
			fake = Faker()
			# model = request.args.get('model')()
			
			if request.args.get('model') == 'categories':

				name = fake.word()
				if Category.query.filter_by(name=name).count() > 0:
					continue

				model = Category()
				model.name = name
				model.parent_id = get_random_elem(Category.query.all())
				
				db.session.add(model)
				db.session.commit()

			if request.args.get('model') == 'products':

				name = fake.word()
				if Product.query.filter_by(name=name).count() > 0:
					continue

				model = Product()
				model.name = name
				model.category_id = get_random_elem(Category.query.all(), False)
				model.price = fake.random_number(4)
				model.prop1 = fake.random_number(1, True)
				model.prop2 = fake.random_number(2, True)
				
				db.session.add(model)
				db.session.commit()
		return redirect('/admin/faker', code=302)

	categories = Category.query.all()
	products = Product.query.all()

	return render_template('admin/faker.html', categories=categories, products=products)


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