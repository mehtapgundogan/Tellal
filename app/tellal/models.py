#from account.models import User
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from flask import Flask
from app import *

class Issue(db.Model):
	__tablename__ = "issue"
	owner=db.Column(db.Integer,db.ForeignKey("user.id"))
	project=db.Column(db.String(256))
	start_date=db.Column(db.DateTime,default=func.now())
	end_date=db.Column(db.DateTime)
	description=db.Column(db.String(128))
	id=db.Column(db.Integer,primary_key=True)
	user_owner = db.relationship("User",
        backref=db.backref("issue"))
