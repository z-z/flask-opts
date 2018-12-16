from app import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False, unique=True)
	price = db.Column(db.Integer, nullable=False, default=0)
	prop1 = db.Column(db.Integer, nullable=False, default=0)
	prop2 = db.Column(db.Integer, nullable=False, default=0)

	category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete='CASCADE'))