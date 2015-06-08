#!/usr/bin/env python

from app import create_app
from flask.ext.script import Manager, Shell


app = create_app()
manager = Manager(app)

@manager.command
def runserver():
	print "calisiyor"
	app.run(host='0.0.0.0', port=83, debug=True)

if __name__ == "__main__":
	manager.run()
