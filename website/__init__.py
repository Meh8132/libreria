from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "libreria.db"

#CONEXION BASE DE DATOS

app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = '0CC175B9C0F1B6A831C399E269772661'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #VERIFICACION DE INGRESO DEL USUARIO

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#CREACION DE LA BASE DE DATOS

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Base de datos creada')