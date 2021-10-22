from app import app
from flask import render_template


@app.route("/exmaple1")
def example1():
    user = { 'name':"Igor Chiesov"}
    return render_template("index.html", title = "pizdec, html", user=user )

@app.route("/")
@app.route("/index")
def index():
    return "This Is just a start page. Try to do /example1, 2, 3"

