#!/usr/bin/env python

from app import create_app, init_app
from flask.ext.script import Manager, Shell

app = init_app()
manager = Manager(app)


@manager.command
def create():
	app = create_app()

@manager.command
def runserver():
	app.run(host='0.0.0.0', port=83, debug=True)

if __name__ == "__main__":
	manager.run()
