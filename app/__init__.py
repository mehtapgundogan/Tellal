#!/usr/bin/python

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
import os, sys

# Define the WSGI application object
app = Flask(__name__)
# Configurations
app.config.from_object('config')
db = SQLAlchemy(app)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "app"))

	
def init_app():
	return app

def create_app():
	# Import a module / component using its blueprint handler variable (mod_auth)	
	#db object
	from app.account import models
	from app.tellal import models
	db.init_app(app)
	db.create_all()
	
	return app
