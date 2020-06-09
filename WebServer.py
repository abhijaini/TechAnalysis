from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<page_name>')
def hello_world(page_name):
    return render_template(page_name)