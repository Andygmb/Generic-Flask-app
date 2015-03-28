from application import app, oid, rs, celery
from models import User, Subreddit, Bans, Attempt
from tasks import check_reddit_oauth, request_steam_api, setflair, check_steamrep
from flask import Flask, session, redirect, request, render_template, url_for
from config import secrets, constants
from flask.ext.openid import OpenID
from celery.result import AsyncResult


@app.route("/arg/")
def return_something(arg):
	return arg