#from account.models import User
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from flask import Flask
from app import db
from account.models import User

import sqlalchemy_utils
from flask.ext.babel import get_locale


sqlalchemy_utils.i18n.get_locale = get_locale

from sqlalchemy_i18n import (
    make_translatable,
    translation_base,
    Translatable,
)


make_translatable(options={'locales': ['tr', 'en']})

class Issue(Translatable,db.Model):
	__tablename__ = "issue"
	__table_args__ = {"useexisting" : True}
	__translatable__ = {'locales': ['tr', 'en']}
    
	id= db.Column(db.Integer,primary_key=True)
	owner = db.Column(db.Integer,db.ForeignKey("user.id"))
	project = db.Column(db.String(256))
	start_date = db.Column(db.DateTime,default=func.now())
	end_date = db.Column(db.DateTime)
	description = db.Column(db.String(128))
