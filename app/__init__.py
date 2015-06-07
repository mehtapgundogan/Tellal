from flask.ext.sqlalchemy import SQLAlchemy
# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://dbtestuser2:dbtestpassword@localhost:3306/dbtest"
db = SQLAlchemy(app)
# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.hello.controllers import mod_hello

# Register blueprint(s)
app.register_blueprint(mod_hello)
# app.register_blueprint(xyz_module)
# ..

