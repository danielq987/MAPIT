from flaskr import app
from flask import Flask, render_template

import sqlite3

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/surveyresults')
def surveyresults():
<<<<<<< HEAD
    return render_template('surveyresults.html')

=======
    db = sqlite3.connect("survey.db")
    rows = db.execute("SELECT * FROM survey")
    print(rows)
    return render_template("surveyresults.html", rows=rows)    
>>>>>>> b5606a26d668132641329b822dfa21611f7c7fd5
