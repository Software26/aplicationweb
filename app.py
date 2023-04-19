from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']='password'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_contact')
def contact():
    return 'add contact'

@app.route('/edit')
def edit():
    return "edit contact"

@app.route("/delete")
def delete():
    return delete



if __name__ == '__main__':
    app.run(debug=True)