import socketio
from app import app, socketio
from flask import render_template
from flask_socketio import emit


posts = []
#simple example of how flask work
@app.route("/")
@app.route("/index")
def index():
    return "This Is just a start page. Try to do /example1, 2, 3"


#here we introduce templates
@app.route("/example1")
def example1():
    user = { 'name':"Igor Chiesov"}
    return render_template("index.html", exNumber = "1", user=user, posts = posts )


@app.route("/example2")
def example2():
    return render_template( 
        "textField.html",  exNumber = "2"
    )

@socketio.on("getMessage", namespace="Main")
def getMessage(msg):
    print(msg)
