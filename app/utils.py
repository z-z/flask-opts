from random import choice

def get_random_elem(objs, nullable=True):
	ids = []
	if nullable:
		ids.append(None)
	for obj in objs:
		ids.append(obj.id)
	return choice(ids)