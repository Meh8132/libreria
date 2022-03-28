from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/carrito')
def carrito():
    return render_template("carrito.html")

@views.route('/producto')
def producto():
    return render_template("producto.html")

@views.route('/usuario')
def usuario():
    return render_template("usuario.html")