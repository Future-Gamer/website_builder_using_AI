# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
# ]
# ///
from flask import Flask, render_template

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/myprojects')
def myprojects():
    return render_template('myprojects.html')

@app.route('/faqs')
def faqs():
    return render_template('FAQs.html')

@app.route('/new-website')
def new_website():
    return render_template('new-website.html')

if(__name__=="__main__"):
    app.run(host="127.0.0.1",port=8080,debug=True)