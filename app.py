# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
# ]
# ///
from flask import Flask

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route('/')
def hello():
    return 'Hello, World!'

if(__name__=="__main__"):
    app.run(host="127.0.0.1",port=8080,debug=True)