# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from forms import BulletinForm

mod_hello = Blueprint('hello', __name__, url_prefix='/hello')

@mod_hello.route('/hello', methods=['GET', 'POST'])
def hello():
	form = BulletinForm(request.form)
	print "hello"
	if request.method == 'POST':
		print "POST"

	return render_template("hello/hello.html", form=form)


@mod_hello.route('', methods=['GET', 'POST'])
def register():
    form = BulletinForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
    	return render_template('hello/hello.html', form=form)
    return render_template('hello/hello.html', form=form)
