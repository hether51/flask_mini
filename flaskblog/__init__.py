from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json,time
#import mysql.connector

# after import app in console , add the context: app.app_context().push()
# or just flask shell
app = Flask(__name__)
app.config['SECRET_KEY'] = '77ceed0246b6184b5fe46f96d72fa4b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy()
db.init_app(app)

from flaskblog import routes