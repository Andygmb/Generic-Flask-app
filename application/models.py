from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from application import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)

	def __init__(self, redditname, steam, ip):
		self.username = username

	def __repr__(self):
		return '<User %s>' % self.username

db.create_all()