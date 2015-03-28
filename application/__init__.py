from config import secrets, constants
from celery import Celery
from flask import Flask
from flask.ext.openid import OpenID
from flask.ext.sqlalchemy import SQLAlchemy

def make_celery(app):
    celery = Celery(app.import_name, backend='amqp', broker='amqp://guest@localhost//')
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs) 
    celery.Task = ContextTask
    return celery


app = Flask(__name__)
oid = OpenID(app)
app.secret_key = secrets.APP_SECRET_KEY
app.debug = constants.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@localhost/databasename'
celery = make_celery(app)
db = SQLAlchemy(app)


from application import views
from application import tasks
