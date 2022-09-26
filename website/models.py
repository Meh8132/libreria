from email.policy import default
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func 

#Generacion de modelos de la base de datos

#Modelo de usario

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(db.String(3))
    email = db.Column(db.String(128), unique=True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    password = db.Column(db.String(40))
    address = db.Column(db.String(80))
    orders = db.relationship('Order')

#Modelo de producto

class Product(db.Model):
    id_prod = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String(20))
    image = db.Column(db.String(20))
    price = db.Column(db.Integer)
    desc = db.Column(db.String(100))
    cat_prod = db.Column(db.Integer, db.ForeignKey('category.id_cat'))
    orders = db.relationship('Order_prod')

#Modelo de categoria

class Category(db.Model):
    id_cat = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20))
    type_cat = db.Column(db.Integer, db.ForeignKey('cat_type.id_cat_type'))
    prod = db.relationship('Product')

class Cat_type(db.Model):
    id_cat_type = db.Column(db.Integer, primary_key=True)
    cat_type = db.Column(db.String(20))
    cat = db.relationship('Category')

class Order(db.Model):
    id_order = db.Column(db.Integer, primary_key=True)
    user_order = db.Column(db.Integer, db.ForeignKey('user.id'))
    products = db.relationship('Order_prod')
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Order_prod(db.Model):
    id_order_prod = db.Column(db.Integer, primary_key=True)
    prod = db.Column(db.Integer, db.ForeignKey('product.id_prod'))
    order = db.Column(db.Integer, db.ForeignKey('order.id_order'))