from flaskr import app
from flask import Flask, render_template

import sqlite3

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/surveyresults')
def surveyresults():
    db = sqlite3.connect("survey.db")
    d = db.cursor()
    rows = d.execute("SELECT * FROM survey")
    return render_template("surveyresults.html", rows=rows)
