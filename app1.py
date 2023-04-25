from flask import Flask,render_template,request,url_for,redirect,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connetion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#Settings
app.secret_key= 'mysecretkey'
#------------
@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template("index.html", contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (Fullname, phone, email) VALUES (%s,%s,%s)',(fullname, phone, email))
        mysql.connection.commit()
        flash('contact Added successfully')
        return redirect(url_for('index'))
    
@app.route('/edit/<id>')
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = %s',(id))
    data = cur.fetchall()
    return render_template("edit_contact.html", contact = data[0])

@app.route("/delete/<string:id>")
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfull')
    return id



if __name__ == '__main__':
    app.run(debug=True)