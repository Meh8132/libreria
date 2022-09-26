from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

#Generacion de las vistas de cada pagina

#Pagina principal

@views.route('/')
def home():
    return render_template("index.html", user=current_user)

#Pagina carrito

@views.route('/carrito')
def carrito():
    return render_template("carrito.html", user=current_user)

#Pagina producto

@views.route('/producto')
def producto():
    return render_template("producto.html", user=current_user)

#Pagina usuario

@views.route('/usuario')
@login_required
def usuario():
    return render_template("usuario.html", user=current_user)