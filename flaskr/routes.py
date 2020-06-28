from flaskr import app
from flask import Flask, redirect, request, render_template

import sqlite3
# import pygeoj

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    # gfile = pygeoj.load(filepath="C:/Users/danie/myproject/MAPIT/flaskr/static/canada.geojson")
    # db = sqlite3.connect("survey.db")

    # sql = db.execute("SELECT location, average from stats")
    # d = ""
    # for row in sql:
    #     d = d + str(row[1])
    return render_template("home.html")

@app.route('/survey', methods=["GET", "POST"])
def survey():

    db = sqlite3.connect("survey.db")

    if request.method == "POST":
        location = request.form.get("location")
        datetime = request.form.get("datetime")
        type_interaction = request.form.get("type_interaction")
        scale = request.form.get("scale")
        add_info = request.form.get("add_info")
        gender = request.form.get("gender")
        age = request.form.get("age")
        race = request.form.get("race")
        education = request.form.get("education")

        sql = ("INSERT INTO survey (location, datetime, type_interaction, scale, add_info, gender, age, race, education) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        db.execute(sql, (location, datetime, type_interaction, scale, add_info, gender, age, race, education))
        db.commit()
    

        sql2 = ("UPDATE stats SET average = (SELECT avg(scale) FROM survey WHERE survey.location = stats.location);")
        db.execute(sql2)
        db.commit()
        db.close()

        return redirect("home")
    else: 
        return render_template("survey.html")
        
        

@app.route('/surveyresults')
def surveyresults():
    db = sqlite3.connect("survey.db")
    d = db.cursor()
    rows = d.execute("SELECT * FROM survey")
    return render_template("surveyresults.html", rows=rows)


@app.route('/stats')
def stats():
    db = sqlite3.connect("survey.db")
    d = db.cursor()
    rows = d.execute("SELECT avg(scale), location  FROM survey GROUP BY location;")
    return render_template("stats.html", rows=rows)
