from time import time
from flaskblog import db
class Sessions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	times = db.Column(db.Float, nullable=False, default=time)
	def __repr__(self):
		return "{}".format(self.times)
