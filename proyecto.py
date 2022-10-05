from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# INICIAR FLASK
app = Flask(__name__)

# CONECCION CON MySQL
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)

# CONFIGURACION
app.secret_key = "mysecretkey"

# RUTAS
@app.route('/')
def Index():
    return render_template('index.html')


#AGREGAR USUARIO
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (fullname, email, username, password) VALUES (%s,%s,%s,%s)", (fullname, email, username, password))
        mysql.connection.commit()
        flash('User Added successfully')
        return redirect(url_for('/html/login.html'))


#EDITAR USUARIO
@app.route('/edit/<username>', methods = ['POST', 'GET'])
def get_contact(username):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users WHERE username = %s', (username))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('index.html', user = data[0])

#ACTUALIZAR USUARIO
@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE users
            SET fullname = %s,
                email = %s,
                username = %s,
                password = %s
            WHERE username = %s
        """, (fullname, email, username, password, username))
        flash('User Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index.html'))


#ELIMINAR USUARIO
@app.route('/delete/<string:username>', methods = ['POST','GET'])
def delete_contact(username):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM users WHERE username = %s'.format(username))
    mysql.connection.commit()
    flash('User Removed Successfully')
    return redirect(url_for('Index.html'))

# INICIAR APP
if __name__ == "__main__":
    app.run(port=3000, debug=True)