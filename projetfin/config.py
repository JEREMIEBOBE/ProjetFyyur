import os
from dotenv import load_dotenv
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
#https://kris-litman.medium.com/connecting-flask-to-a-mysql-database-6f4d71b85d4e
load_dotenv()

db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://{db_user}:{db_password}@localhost:5432/{db_name}".format(
    db_user=db_user, db_password=db_password, db_name=db_name)

SQLALCHEMY_TRACK_MODIFICATIONS = False