from app import app, socketio
from flask import render_template, request, jsonify
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
        "example2.html",  exNumber = "2"
    )

@app.route("/example3", methods = ['GET','POST'])
def example3():
    if request.method == 'POST':
        content = request.json
        print(content['msg'])
        return jsonify(success =True)
    else:
        return render_template( 
            "example3.html",  exNumber = "3"
        )

    
@socketio.on('connect',namespace = '/main')
def test_connect():
    print("we have connection")

@socketio.on('getMessage',namespace = '/main')
def getMessage(message):
    print(message['message'])
    emit("confirmer",message)
