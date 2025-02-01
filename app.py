from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func
import sqlite3
from functools import wraps

from ai import get_list_of_pages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
app.secret_key = "asd"

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    email = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String(75), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

# Decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Execute query to check for user
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    
    if user:
        session['username'] = username
        return redirect(url_for('new_website'))
    else:
        return 'Invalid credentials, please try again.'

@app.route('/plan')
@login_required
def plan():
    return render_template('plan.html')

@app.route('/myprojects')
@login_required
def myprojects():
    return render_template('myprojects.html')

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Add user registration logic here
        pass
    return render_template('signup.html')

@app.route('/new-website')
@login_required
def new_website():
    return render_template('new-website.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('hello'))

@app.route('/gen-list',methods=["POST"])
def gen_list():
    str1= f"""You are WebAI. You are designed as the world's best web designer and creator. You interpret user requests and use them to generate beatiful, responsive websites.
List all the pages that will be needed to make the website. List them in a format similar to `/index.html - [Home Page]`. DO NOT generate anything else.

Website Name: {request.form['name']}
Website Description: {request.form['desc']}
"""
    str1=get_list_of_pages(str1)
    print(str1)
    return str(str1)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
