from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
app.secret_key="asd"

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    email = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String(75), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if(request.method=="GET"):
        return render_template("login.html")
    
    print(request.form.keys())
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Log the query being executed
    print(f"Executing query to check for user: {username}")
    
    # Execute query to check for user
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    
    # Log the query result
    print(f"Query result: {user}")
    
    if user:
        session['username'] = username
        
        return redirect('/new-website')
    else:
        return 'Invalid credentials, please try again.'
    
    

# @app.route('/login', methods=['POST'])


@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/myprojects')
def myprojects():
    return render_template('myprojects.html')

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/new-website')
def new_website():
    return render_template('new-website.html')

if(__name__=="__main__"):
    app.run(host="127.0.0.1",port=8080,debug=True)