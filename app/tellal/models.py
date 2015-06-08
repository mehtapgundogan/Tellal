#from account.models import User
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from flask import Flask
from app import db
from account.models import User

class Issue(db.Model):
	__tablename__ = "issue"
	__table_args__ = {"useexisting" : True}
	id= db.Column(db.Integer,primary_key=True)
	owner = db.Column(db.Integer,db.ForeignKey("user.id"))
	project = db.Column(db.String(256))
	start_date = db.Column(db.DateTime,default=func.now())
	end_date = db.Column(db.DateTime)
	description = db.Column(db.String(128))
