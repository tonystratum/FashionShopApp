from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from fashionshop.admin_views import MyModelView, DashboardView
from datetime import timedelta
from elasticsearch import Elasticsearch
import os

# postgresql cfg
USER = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
DB_NAME = "fsapp"

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.permanent_session_lifetime = timedelta(minutes = 20)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}'
es = Elasticsearch()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
admin = Admin(app, index_view=DashboardView())
from fashionshop.models import *
from fashionshop import routes

db.create_all()
db.session.commit()

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Product, db.session))
admin.add_view(MyModelView(CartItem, db.session))
admin.add_view(MyModelView(Category, db.session))
