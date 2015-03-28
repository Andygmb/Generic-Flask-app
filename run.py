from application import app
from application.constants import secrets

if __name__ == "__main__":
	app.run(secrets.DEBUG)
