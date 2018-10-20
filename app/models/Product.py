from app import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False, unique=True)

	category_id = db.Column(db.Integer, db.ForeignKey("category.id"))