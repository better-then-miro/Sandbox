from app import app, socketio, ServerController
from flask import render_template, request, jsonify, Response
from flask_socketio import emit
import json

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


@socketio.on("getDiagramContent", namespace="/main")
def getDiagramContent(content):
    dId = content["Id"]
    if dId is not None:
        dia = ServerController.getDiagramContentByDID(dId)
        #TODO we kinda want to add user to room here
        if dia is not None:
            emit("getDiagramContentHandler", json.dumps(
                dia.serializeContent()
            ))

    return emit("getDiagramContentHandler", {})

#возможно все 4 запроса могут быть одним 
#и нам достаточно указывать тип модифицируемого объекта
@socketio.on("updateBlockProperties", namespace="/main")
def updateBlockProperties(content):
    if content is not None and ServerController.modifyBlockById(content):
        emit("updateBlockPropertiesHandler", jsonify(success = True))
    #TODO figure out what we are supposed to send here
    #else:
    #    return Response(status = 422)

@socketio.on("updateLinkProperties", namespace= "/main")
def modifyLinkById(content):
    if content is not None and ServerController.modifyLinkById(content):
        emit("updateLinkPropertiesHandler", jsonify(success = True))
    #else:
    #    return Response(status = 422)     


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

@socketio.on("createNewBlock", namespace = '/main')
def createNewBlock(content):
    if content is not None:
        bId = ServerController.addBlock(content)
        if bId is not None:
            emit('createNewBlockHandler', jsonify({"bId":bId}))
    else:
        print('content was None')

@socketio.on("createNewLink", namespace = '/main')
def createNewLink(content):
    if content is not None:
        lId = ServerController.addLink(content)
        if lId is not None:
            emit('createNewLinkHandler', jsonify({"lId":lId}))
    else:
        print('content was None')

@socketio.on("deleteBlock", namespace = '/main')
def deleteBlock(content):
    res = ServerController.deleteBlock(content)
    if res:
        emit('deleteBlockHandler', jsonify(success = True))
    else:
        print('content was None')

@socketio.on("deleteLink", namespace = '/main')
def deleteLink(content):
    res = ServerController.deleteLink(content)
    if res:
        emit('deleteLinkHandler', jsonify(success = True))
    else:
        print('content was None')

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
