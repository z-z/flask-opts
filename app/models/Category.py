from app import db

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False, unique=True)

	products = db.relationship('Product', backref="category", cascade="all,delete-orphan")

	parent_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=True)
	parent = db.relationship('Category', backref=db.backref("sub_categories", cascade="all,delete"), remote_side=id, single_parent=True)

		
