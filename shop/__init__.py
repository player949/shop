# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('app.conf')
app.secret_key = 'wgy'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = '/regloginpage/'

from B2B import views, models

#  todo finish that serach problem finish the big data problemto be a good leader  and how??how to finish it
# people is the problem

