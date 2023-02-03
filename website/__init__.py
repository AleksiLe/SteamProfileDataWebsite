from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

dp = SQLAlchemy()
DP_NAME="database.dp"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Hard to guess string!' #Should not be shown
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DP_NAME}'
    dp.init_app(app)
    
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
