from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)  

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method ==  'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Ingreso', category='success ')
                return redirect(url_for('views.home'))
            else:
                flash('Contraseña incorrecta', category='error')
        else:
            flash('Correo no registrado', category='error')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email1 = request.form.get('email1')
        email2 = request.form.get('email2')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        address = request.form.get('address')

        user = User.query.filter_by(email=email1).first()

        if user:
            flash('Correo electronico ya registrado')

        elif len(email1) < 6:
            flash('El correo debe tener mas de 6 caracteres', category='error')
        elif len(firstname) < 2:
            flash('El nombre debe tener mas de 6 caracteres', category='error')
        elif len(lastname) < 2:
            flash('El apellido debe tener mas de 6 caracteres', category='error')
        elif password1 != password2:
            flash('Las contraseñas no coinciden', category='error')
        elif len(password1) < 7:
            flash('La contraseña debe tener mas de 7 caracteres', category='error')
        elif email1 != email2:
            flash('Los correos no coinciden', category='error')
        elif len(address) < 8:
            flash('La direccion debe tener mas de 8 caracteres', category='error')
        else:
            new_user = User(email=email1, firstname=firstname, lastname=lastname,  password=generate_password_hash(password1, method='sha256'), address=address)
            db.session.add(new_user)
            db.session.commit()
            flash('Cuenta creada satisfactoriamente', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")
