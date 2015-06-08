#!/usr/bin/python

from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask


def create_app():
	# Define the WSGI application object
	app = Flask(__name__)
	# Configurations
	app.config.from_object('config')
	
	#db object
	db = SQLAlchemy(app)
	db.init_app(app)

	# Import a module / component using its blueprint handler variable (mod_auth)
	from app.hello.controllers import mod_hello
	
	# Register blueprint(s)
	app.register_blueprint(mod_hello)
	# app.register_blueprint(xyz_module)
	# ..
	return app
