from flaskr import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    return ("Hello World")

@app.route('/survey')
def survey():
    return render_template('survey.html')
