"""
Routes and views for the flask application.
"""
from flask import *
from login import app
import mysql.connector




mydb = mysql.connector.connect(
    user="siying@fypdemo",                           
    password="QWERTY123ytrewq", 
    host="fypdemo.mysql.database.azure.com", 
    port=3306,
    database = "fyp"
    )
print(mydb)
    
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM admin")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)



@app.route('/')
@app.route('/login')
def home():
    """Renders the home page."""
    return render_template('layout.html')
   


@app.route('/index', methods=['POST'])
def login():
    """Renders the login success page."""
    usrname = request.form["password"]
    pwd = request.form["username"]
    statement = String.format("SELECT login_id, login_passwd FROM admin WHERE login_id = '%s' AND lgin_passwd = '%s'")
    mycursor.execute(statement)
    result = mycursor.fetchall()
    if myresult.length != 0:
        return render_template('Index.html')
    else:
        return redirect('/login')
        flash("Username or password is incorrect")

