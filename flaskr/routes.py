from flaskr import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/survey')
def survey():
    return render_template('survey.html')
