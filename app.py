from flask import Flask,render_template,request
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

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        return 'Formulary update'
    
@app.route('/edit')
def edit():
    return "edit contact"

@app.route("/delete")
def delete():
    return "delete"



if __name__ == '__main__':
    app.run(debug=True)