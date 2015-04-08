# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

mod_hello = Blueprint('hello', __name__, url_prefix='/hello')

@mod_hello.route('/', methods=['GET', 'POST'])
def hello():
	print "hello"
	return render_template("hello/hello.html")
