from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os


app=Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI') if os.environ.get('SQLALCHEMY_DATABASE_URI') else "sqlite:///site.db"
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

from CMS.GetRequests.routes import get
from CMS.User.routes import user
from CMS.PostRequests.routes import post
from CMS.PutRequests.routes import put
from CMS.DeleteRequests.routes import delete

app.register_blueprint(get)
app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(put)
app.register_blueprint(delete)
