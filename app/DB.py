from werkzeug.utils import validate_arguments
from app import entities
from app import DataBase

import copy

database = DataBase.DataBase(DataBase.DATABASEMODE.MEMORY)
blockExample = entities.Block(0,"Class",200,50,50,50)
projectExample = entities.Project(0, "test 0","Project 0" )
diagramExample = entities.Diagram(0, "Diagram 0", "-","use-case","Strict")
linkExample = entities.Link(0,"Association", 0,1)

def getProjects():
    return database.getProjects()

def getDiagramsByProject(pId):
    try:
        pId = int(pId)
    except ValueError:
        return None

    return database.getDiagrams(pId)

def getDiagramContentByDID(dId):
    try:
        dId = int(dId)
    except ValueError:
        return None
    return database.getDiagramsContent(dId)

def modifyBlockById(content):
    if "Id" in content.keys():
        try:
            bId = int( content["Id"])
        except ValueError:
            return False
        if set(content.keys()).issubset(vars(blockExample).keys()):
            return database.modifyBlock(content,bId)
        
    return False

def modifyLinkById(content):
    if "Id" in content.keys():
        try:
            lId = int( content["Id"])
        except ValueError:
            return False
        
        if set(content.keys()).issubset(vars(linkExample).keys()):
            return database.modifyLink(content,lId)
    return False

def modifyProjectById(content):
    if "Id" in content.keys():
        try:
            pId = int( content["Id"])
        except ValueError:
            return False
        if set(content.keys()).issubset(vars(projectExample).keys()):
            return database.modifyProject(content,pId)
            
    return False

def modifyDiagramById(content):
    if "Id" in content.keys():
        try:
            dId = int( content["Id"])
        except ValueError:
            return False
        
        if set(content.keys()).issubset(vars(diagramExample).keys()):
            return database.modifyDiagram(content,dId)
    return False

def addProject(content):
    keys = content.keys()
    name = content["name"] if "name" in keys else ""
    description= content["description"] if "description" in keys else ""
    
    return database.addNewProject(entities.Project(None,name, description))
    

def addDiagram(content):
    
    keys = content.keys()
   
    name = content["name"] if "name" in keys else ""
    
    try:
        pId = int(content["pId"]) if "pId" in keys else None
    except ValueError:
        return None
    
    Type = content["Type"] if "Type" in keys else ""
    description= content["description"] if "description" in keys else ""
    mode = content["mode"] if "mode" in keys else "free"

    if pId is None or Type is None:
        return None
     
    return database.addNewDiagram(entities.Diagram(None, name, description, Type, mode), pId)
    
def addBlock(content):
    keys = content.keys()
    Type = content["Type"] if "Type" in keys else None
    try:
        coords = (int(content["coords"][0]), int(content["coords"][1]) ) if "coords" in keys else None
        width = int(content["width"]) if "width" in keys else None
        height = int(content["height"]) if "height" in keys else None
        dId = int(content["dId"]) if "dId" in keys else None
    except ValueError:
        return None
    if Type is None or coords is None or width is None or height is None or dId is None:
        return None
    
    title = content["title"] if "title" in keys else ""
    description = content["description"] if "description" in keys else ""
    additionalFields = content["additionalFields"] if "additionalFields" in keys else {}
    
    
    return database.addNewBlock(entities.Block(None, Type, coords[0], coords[1], width, height, description, title, additionalFields),dId)
    

def addLink(content):
    keys = content.keys()
    Type = content["Type"] if "Type" in keys else None
    try:
        dId = int(content["dId"]) if "dId" in keys else None
        sId = int(content["sId"]) if "sId" in keys else None
        tId = int(content["tId"]) if "tId" in keys else None
    except ValueError:
        print("error")
        return None
    if Type is None or sId is None or tId is None or dId is None:
        print(Type, sId, tId, dId)
        return None 
    return database.addNewLink(entities.Link(None, Type, sId, tId),dId)
    