from app import app, socketio, ServerController
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
        [project.serialize() for project in ServerController.getProjects()]
    )

@app.route("/getDiagrams", methods = ['GET'])
def getDiagrams():
    pId = request.args.get("Id")
    if pId is not None:
        dias = ServerController.getDiagramsByProject(pId)
        if dias is not None:
            return jsonify(
                [dia.serializeInfo() for dia in dias]
            )
    
    return Response(status=422)

@app.route("/getDiagramContent", methods = ['GET'])
def getDiagramContent():
    dId = request.args.get("Id")
    if dId is not None:
        dia = ServerController.getDiagramContentByDID(dId)
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
    if content is not None and ServerController.modifyBlockById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)

@app.route("/updateDiagramProperties", methods = ['POST'])
def updateDiagramProperties():
    content = request.json
    if content is not None and ServerController.modifyDiagramById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)

@app.route("/updateProjectProperties", methods = ['POST'])
def updateProjectProperties():
    content = request.json
    if content is not None and ServerController.modifyProjectById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)      

@app.route("/updateLinkProperties", methods = ['POST'])
def modifyLinkById():
    content = request.json
    if content is not None and ServerController.modifyLinkById(content):
        return jsonify(success = True)
    else:
        return Response(status = 422)     


@app.route("/createNewProject", methods = ['POST'])
def createNewProject():
    content = request.json
    if content is not None:
        return jsonify( {"pId" : ServerController.addProject(content)})
    else:
        return Response( status = 422 )

@app.route("/createNewDiagram", methods = ["POST"])
def createNewDiagram():
    content = request.json
    
    if content is not None:
        dId = ServerController.addDiagram(content)
        if dId is not None:
            return jsonify({"dId": dId})    
    return Response(status = 422)

@app.route("/createNewBlock",methods = ["POST"])
def createNewBlock():
    content = request.json
    
    if content is not None:
        bId = ServerController.addBlock(content)
        if bId is not None:
            return jsonify({"bId":bId})
    return Response(status = 422)


@app.route("/createNewLink",methods = ["POST"])
def createNewLink():
    content = request.json
    
    if content is not None:
        lId = ServerController.addLink(content)
        if lId is not None:
            return jsonify({"lId":lId})
    return Response(status = 422)

@app.route("/deleteBlock", methods = ["DELETE","GET"] )
def deleteBlock():
    if request.method == 'DELETE':
        res = ServerController.deleteBlock(content = request.json)
    elif request.method == "GET":
        res = ServerController.deleteBlock(bId = request.args.get("Id"))
    if res:
        return jsonify(success = True)
    return Response(status = 422)

@app.route("/deleteLink", methods = ["DELETE","GET"] )
def deleteLink():
    if request.method == 'DELETE':
        res = ServerController.deleteLink(content = request.json)
    elif request.method == "GET":
        res = ServerController.deleteLink(lId = request.args.get("Id"))
    if res:
        return jsonify(success = True)
    return Response(status = 422)

@app.route("/deleteDiagram", methods = ["DELETE","GET"] )
def deleteDiagram():
    if request.method == 'DELETE':
        res = ServerController.deleteDiagram(content = request.json)
    elif request.method == "GET":
        res = ServerController.deleteDiagram(dId = request.args.get("Id"))
    if res:
        return jsonify(success = True)
    return Response(status = 422)

@app.route("/deleteProject", methods = ["DELETE","GET"] )
def deleteProject():
    if request.method == 'DELETE':
        res = ServerController.deleteProject(content = request.json)
    elif request.method == "GET":
        res = ServerController.deleteProject(pId = request.args.get("Id"))
    if res:
        return jsonify(success = True)
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
