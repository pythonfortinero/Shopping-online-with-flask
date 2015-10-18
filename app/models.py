from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime


class SalesOrder(db.Model):

	__tablename__ = "salesOrder"
	
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime, default=datetime.datetime.now)
	salesOrderRow = relationship("SalesOrderRow", backref="salesOrder")

	def __init__(self):
		pass

	def __repr__(self):
		pass

class SalesOrderRow(db.Model):

	__tablename__ = "salesOrderRow"

	id = db.Column(db.Integer, primary_key=True)
	itemName = db.Column(db.String, nullable=False)
	qty = db.Column(db.Integer, nullable=False)
	sales_id = db.Column(db.Integer, ForeignKey('salesOrder.id'))

	def __init__(self, itemName, Qty):
		self.itemName = itemName
		self.qty = Qty

	def __repr__(self):
		pass