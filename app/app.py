from flask import Flask, flash, redirect, render_template, json, request, url_for,app
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.mysql import MySQL
#from flask_mysql import MySQL
#import MySQLdb
app.secret_key = 'random string'
app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
   return render_template('login.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    # create user code will be here !!

    # read the posted values from the UI
    _name = request.form['inputName']
    _username = request.form['inputUserName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _confirmpassword = request.form['inputConfirmPassword']
    _DD = request.form['inputDD']
    _MM = request.form['inputMM']
    _YYYY = request.form['inputYYYY']
    _location = request.form['inputlocation']
    
 
    # validate the received values
    if _name and _username and _Email and _password and _ConfirmPassword and _DD and _MM and _YYYY and _location:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})



@app.route('/showSignIn', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
			
   return render_template('login.html', error = error)

if __name__ == "__main__":
   app.run(debug = True)
