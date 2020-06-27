from flaskr import app
from flask import Flask, redirect, request, render_template

import sqlite3

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/survey', methods=["GET", "POST"])
def survey():

    db = sqlite3.connect("survey.db")

    if request.method == "POST":
        location = request.form.get("location")
        datetime = request.form.get("datetime")
        gender = request.form.get("gender")
        
        sql = ("INSERT INTO survey (location, datetime, gender) VALUES (?, ?, ?)")
        db.execute(sql, (location, datetime, gender))
        db.commit()
        db.close()

        return redirect("/")
    else: 
        return render_template("survey.html")
        
        

@app.route('/surveyresults')
def surveyresults():
    db = sqlite3.connect("survey.db")
    rows = db.execute("SELECT * FROM survey")
    return render_template("surveyresults.html", rows=rows)    
