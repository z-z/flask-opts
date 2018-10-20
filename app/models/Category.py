from app import db
# from app.models import Product

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False, unique=True)

	products = db.relationship('Product')

	parent_id = db.Column(db.Integer, db.ForeignKey("category.id"))
	parent = db.relationship('Category', backref="children", remote_side=id)

		
