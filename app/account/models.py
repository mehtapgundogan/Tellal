#from account.models import User
from sqlalchemy.sql import func
from flask import Flask
from app import *

class User(db.Model):
	__tablename__ = "user"
	__table_args__ = {"useexisting" : True}
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(128))
	email = db.Column(db.String(128))
