from app import app, socketio, ServerController, diagramVersions
from flask import render_template, request, jsonify, Response
from flask_socketio import emit, join_room, leave_room



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
            res = dia.serializeContent()
            res["code"] = 200
            join_room(dia.Id)
            if dia.Id not in diagramVersions.keys():
                diagramVersions[dia.Id] = 0 
            res["version"] = diagramVersions[dia.Id]
            print("joined to ",dia.Id)
            emit("getDiagramContentHandler", res)
    else:
        emit("getDiagramContentHandler", {"code":422})

#возможно все 4 запроса могут быть одним 
#и нам достаточно указывать тип модифицируемого объекта
@socketio.on("updateBlockProperties", namespace="/main")
def updateBlockProperties(content):
    if content is not None :
        Id = ServerController.getDiagramIdFromBlock(content)
        copy = content.copy()
        if Id is not None and ServerController.modifyBlockById(content):
            emit("updatePropertiesHandler", {"code": 200})
            copy["code"] = 200
            diagramVersions[Id] += 1
            copy["version"] = diagramVersions[Id] 
            emit("updatePropertiesHandler", copy, to = Id)
    #TODO figure out what we are supposed to send here
    else:
        emit("updatePropertiesHandler", {"code": 422})
    
@socketio.on("updateLinkProperties", namespace= "/main")
def modifyLinkById(content):
    if content is not None :
        Id = ServerController.getDiagramIdFromLink(content)
        copy = content.copy()
        if Id is not None and ServerController.modifyLinkById(content):
            emit("updateLinkPropertiesHandler", {"code": 200})
            copy["code"] = 200
            diagramVersions[Id] += 1
            copy["version"] = diagramVersions[Id]
            emit("updateLinkPropertiesHandler", copy, to = Id)
    else:
        emit("updateLinkPropertiesHandler", {"code": 422})
    
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
            dId = ServerController.database.getDiagramFromBlock(bId)
            emit('createNewBlockHandler', {"code":200, "bId":bId})
            content["Id"] = bId
            diagramVersions[dId] += 1
            content["version"] = diagramVersions[dId]
            emit('spawnNewBlockHandler', content, to = dId)
    else:
        emit('createNewBlockHandler', {"code":422})
    
@socketio.on("createNewLink", namespace = '/main')
def createNewLink(content):
    if content is not None:
        lId = ServerController.addLink(content)
        if lId is not None:
            dId = ServerController.database.getDiagramFromLink(lId)
            emit('createNewLinkHandler', {"code":200, "lId":lId})
            content["Id"] = lId
            diagramVersions[dId] += 1
            content["version"] = diagramVersions[dId]
            emit("spawnNewLinkHandler", content, to=dId)
    else:
        emit('createNewLinkHandler', {"code":422})
    
@socketio.on("deleteBlock", namespace = '/main')
def deleteBlock(content):
    dId = ServerController.database.getDiagramFromBlock(content['Id'])
    res = ServerController.deleteBlock(content)
    if res:
        diagramVersions[dId] += 1
        emit('deleteBlockHandler', {"code":200, 'bId':content['Id'], "version":diagramVersions[dId]}, to=dId)
    else:
        emit('deleteBlockHandler', {"code":422})

@socketio.on("deleteLink", namespace = '/main')
def deleteLink(content):
    dId = ServerController.database.getDiagramFromLink(content['Id'])
    res = ServerController.deleteLink(content)
    if res:
        diagramVersions[dId] += 1
        emit('deleteLinkHandler', {"code":200, 'lId':content['Id'],"version":diagramVersions[dId]}, to=dId)
    else:
        emit('deleteLinkHandler', {"code":422})
    
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

#@app.route("/debug", methods = ["POST"])
#def getSuka():
#    
#    bId = request.json["bId"]
#    ServerController.database.get
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
