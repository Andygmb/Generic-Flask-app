from application import app, rs, celery, reddit, db
from models import username
from celery import Celery
from config import secrets, constants

#celery -A application.celery worker --loglevel=INFO

@celery.task(rate_limit='30/m')
def do_something(arg):
	return arg