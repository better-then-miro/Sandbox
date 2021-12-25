from app import app, socketio, DB
from flask import render_template, request, jsonify, Response
from flask_socketio import emit


posts = []

@app.route("/")
@app.route("/index")
def index():
    return app.send_static_file('index.html')


@app.route("/example2", methods = ['GET'])
def example2():
    return jsonify(success = True)

@app.route("/getProjectList", methods = ['GET'])
def getProjectList():
    return jsonify(
        [project.serialize() for project in DB.getProjects()]
    )

@app.route("/getDiagrams", methods = ['GET'])
def getDiagrams():
    pId = request.args.get("Id")
    if pId is not None:
        dias = DB.getDiagramsByProject(pId)
        if dias is not None:
            return jsonify(
                [dia.serializeInfo() for dia in dias]
            )
    
    return Response(status=422)

@app.route("/getDiagramContent", methods = ['GET'])
def getDiagramContent():
    dId = request.args.get("Id")
    if dId is not None:
        dia = DB.getDiagramContentByDID(dId)
        if dia is not None:
            return jsonify(
                dia.serializeContent()
            )

    return Response(status=422)

#возможно все 4 запроса могут быть одним 
#и нам достаточно указывать тип модифицируемого объекта
@app.route("/updateBlockProperties", methods = ['POST'])
def updateBlockProperties():
    content = request.json
    if content is not None and DB.modifyBlockById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)

@app.route("/updateDiagramProperties", methods = ['POST'])
def updateDiagramProperties():
    content = request.json
    if content is not None and DB.modifyDiagramById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)

@app.route("/updateProjectProperties", methods = ['POST'])
def updateProjectProperties():
    content = request.json
    if content is not None and DB.modifyProjectById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)      

@app.route("/updateLinkProperties", methods = ['POST'])
def modifyLinkById():
    content = request.json
    if content is not None and DB.modifyLinkById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)     


@app.route("/createNewProject", methods = ['POST'])
def createNewProject():
    content = request.json
    if content is not None:
        return jsonify( {"pId" : DB.addProject(content)})
    else:
        return Response( status = 422 )

@app.route("/createNewDiagram", methods = ["POST"])
def createNewDiagram():
    content = request.json
    
    if content is not None:
        dId = DB.addDiagram(content)
        if dId is not None:
            return jsonify({"dId": dId})    
    return Response(status = 422)

@app.route("/createNewBlock",methods = ["POST"])
def createNewBlock():
    content = request.json
    
    if content is not None:
        bId = DB.addBlock(content)
        if bId is not None:
            return jsonify({"bId":bId})
    return Response(status = 422)


@app.route("/createNewLink",methods = ["POST"])
def createNewLink():
    content = request.json
    
    if content is not None:
        lId = DB.addLink(content)
        if lId is not None:
            return jsonify({"lId":lId})
    return Response(status = 422)

# legacy
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
