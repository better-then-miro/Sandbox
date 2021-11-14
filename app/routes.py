from app import app, socketio
from flask import render_template, request, jsonify
from flask_socketio import emit


posts = []
#simple example of how flask work
@app.route("/")
@app.route("/index")
def index():
    return app.send_static_file('index.html')


@app.route("/example2", methods = ['GET'])
def example2():
    return jsonify(success = True)

@app.route("/getDiagrams", methods = ['GET'])
def getDiagrams():
    print("Diagrams request")
    return jsonify([
                 {'diagramID': 1, 'projectID': 1,
                 'name': 'ProjectFromGet_1', 'description': 'test 1', 'type': 'strict'},
                 {'diagramID': 2, 'projectID': 2,
                 'name': 'ProjectFromGet_2', 'description': 'test 2', 'type': 'free'}])

@app.route("/example3", methods = ['GET','POST'])
def example3():
    if request.method == 'POST':
        content = request.json
        print(content['msg'])
        return jsonify(success = True)
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
