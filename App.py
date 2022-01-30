#from contextlib import ContextDecorator
#from crypt import methods
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask ( __name__ )
#MySQL coneccion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontact'
mysql = MySQL(app)

#setting
#Ni idea para lo que es, pero es como un token
app.secret_key = 'mysecretkey'

#@pp se llama decorador, si entra a la ruta raiz,
#ejecuta funcion Index que renderiza index.html, no es
# necesario indicar el la ruta por que sabe que esta en template 
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    #La siguiente linea retorna una variable contact que tiene valor de data
    return render_template('index.html', contacts = data)

#ruta para post
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        #Asigna valores a variables extraido de los input del form html
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        #crea una coneccion y la envia a una variable cur (cursos)
        cur = mysql.connection.cursor()
        #escribe lña consulta sql
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',(fullname, phone, email))
        #ejecuta la coinsulta sql
        mysql.connection.commit()
        #Manda un mensaque flask desde al servidor al frontend, de exito de la transaccion
        flash('Constact addes successfully')
        #despues de ejecutar la coinsulta sql, redirecciona la web a index
        return redirect(url_for('Index'))

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        #Asigna valores a variables extraido de los input del form html
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        #crea una coneccion y la envia a una variable cur (cursos)
        cur = mysql.connection.cursor()
        #escribe lña consulta sql
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
            phone = %s,
            email = %s
            WHERE id = %s
            """ ,(fullname, phone, email, id))
        #ejecuta la coinsulta sql
        mysql.connection.commit()
        #Manda un mensaque flask desde al servidor al frontend, de exito de la transaccion
        flash('Contact updated successfully')
        #despues de ejecutar la coinsulta sql, redirecciona la web a index
        return redirect(url_for('Index'))

#ruta put, recibe id como parametro pero no especifica el tipo de dato
@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = (%s)', [id])
    data = cur.fetchall()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])
    print(id)
    #return 'hello edit'


#ruta delete, rescata el id en el params de la url
@app.route('/delete/<string:id>')
def delete(id):
    cur = mysql.connection.cursor()
    #escribe lña consulta sql, en este caso dice que el id posicion cero
    #sea formato variable id que recibio de los parametros
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    #ejecuta la coinsulta sql
    mysql.connection.commit()
    #Manda un mensaque flask desde al servidor al frontend, de exito de la transaccion
    flash('Constact Removed successfully')
    #despues de ejecutar la coinsulta sql, redirecciona la web a index
    return redirect(url_for('Index'))

#si el archjivo que arranca es app.py, arranca el server
if __name__ == '__main__':
    app.run(port = 3000, debug = True )











