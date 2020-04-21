from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, static_folder='static/files')
app.config['SECRET_KEY'] = 'secret'
db_path = os.path.join(os.path.dirname(__file__), 'site.db')
db_uri = 'sqlite:////{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_ECHO'] = True


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



from myblog import routes

