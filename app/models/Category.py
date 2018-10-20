from app import db

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False, unique=True)

	products = db.relationship('Product', backref="category")

	parent_id = db.Column(db.Integer, db.ForeignKey("category.id"))
	parent = db.relationship('Category', backref="sub_categories", remote_side=id)

		
