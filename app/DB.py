from werkzeug.utils import validate_arguments
from app import entities
import copy


Projects = [
    entities.Project(0, "test 0","Project 0" ),
    entities.Project(1, "test 1","Project 1" ),
    entities.Project(2, "test 2","Project 2" )
]

Diagrams = [
    entities.Diagram(0, "Diagram 0", "-","Strict"),
    entities.Diagram(1, "Diagram 1", "-","Strict"),
    entities.Diagram(2, "Diagram 2", "-","Free"),
    entities.Diagram(3, "Diagram 3", "-","Free")
] 

Blocks = [
    entities.Block(0,"Class",200,50,50,50, 'Controller', '', additionalFields=
    {
        'Operations': ['AddNewBlock(blockId)', 'AddNewLink(linkId)'],
        'Attributes': ['linkType', 'sourceeLinkId', 'targetLinkId']
    }),
    entities.Block(1,"Class",100,60,50,70, 'Link', '', additionalFields=
    {
        'Attributes': ['lId', 'type', 'sourceId', 'targetId']
    }),
    entities.Block(2,"Class",300,40,100,70),
    entities.Block(3,"Class",150,100,50,40),
    entities.Block(4,"Actor",100,200,60,100),
    entities.Block(5,"Use-case",200,250,100,100),
]

Links = [
    entities.Link(0,"Association", 0,1),
    entities.Link(1,"Association", 1,4),
    entities.Link(2,"Association", 1,5),
    entities.Link(3,"Include", 3,2),
]


DiagramToBlock = [
    (0,0),
    (0,1),
    (0,4),
    (0,5),
    (1,2),
    (1,3)
]

DiagramToLink = [
    (0,0),
    (0,1),
    (0,2),
    (1,3)
]

ProjectToDiagrams = [
    (0,0),
    (0,3),
    (1,1),
    (2,2)
]

def getProjects():
    return Projects

def getDiagramsByProject(pId):
    if pId >= len(Projects) or pId < 0:
        return None 
    return [Diagrams[dId] for (ppId,dId) in ProjectToDiagrams if ppId==pId]

def getDiagramContentByDID(dId):
    if dId >= len(Diagrams) or dId < 0:
        return None
    dia = copy.copy(Diagrams[dId])
    dia.blocks = [Blocks[bId] for (ddId, bId) in DiagramToBlock if ddId==dId]
    dia.links = [Links[lId] for (ddId, lId) in DiagramToLink if ddId==dId]
    return dia

def modifyBlockById(content):
    if "Id" in content.keys():
        try:
            bId = int( content["Id"])
        except ValueError:
            return False
        if bId >= len(Blocks) or bId < 0:
            return False
        if set(content.keys()).issubset(vars(Blocks[bId])):
            for key in content.keys():
                setattr(Blocks[bId],key,content[key])
            return True
        
    return False

def modifyLinkById(content):
    if "Id" in content.keys():
        try:
            lId = int( content["Id"])
        except ValueError:
            return False
        if lId >= len(Links) or lId < 0:
            return False
        if set(content.keys()).issubset(vars(Links[lId])):
            for key in content.keys():
                setattr(Links[lId],key,content[key])
            return True
    return False

def modifyProjectById(content):
    if "Id" in content.keys():
        try:
            pId = int( content["Id"])
        except ValueError:
            return False
        if pId >= len(Projects) or pId < 0:
            return False
        if set(content.keys()).issubset(vars(Projects[pId])):
            for key in content.keys():
                setattr(Projects[pId],key,content[key])
            return True
    return False

def modifyDiagramById(content):
    if "Id" in content.keys():
        try:
            dId = int( content["Id"])
        except ValueError:
            return False
        if dId > len(Diagrams) or dId < 0:
            return False
        if set(content.keys()).issubset(vars(Diagrams[dId])):
            for key in content.keys():
                setattr(Diagrams[dId],key,content[key])
            return True
    return False

def addProject(content):
    keys = content.keys()
    name = content["name"] if "name" in keys else ""
    description= content["description"] if "description" in keys else ""
    pId = len(Projects)
    Projects.append(entities.Project(pId,name, description))
    return pId

def addDiagram(content):
    
    keys = content.keys()
   
    name = content["name"] if "name" in keys else ""
    
    try:
        pId = int(content["pId"]) if "pId" in keys else None
    except ValueError:
        return None
    Type = content["Type"] if "Type" in keys else ""
    description= content["description"] if "description" in keys else ""

    if pId is None or Type is None or pId >= len(Projects) or pId < 0 :
        return None
    
    dId = len(Diagrams)
    Diagrams.append(entities.Diagram(len(Diagrams), name, description, Type))
    ProjectToDiagrams.append((pId,dId))
    return dId

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
    if Type is None or coords is None or width is None or height is None or dId is None or dId >= len(Diagrams) or dId < 0:
        return None
    bId = len(Blocks)
    title = content["title"] if "title" in keys else ""
    description = content["description"] if "description" in keys else ""
    additionalFields = content["additionalFields"] if "additionalFields" in keys else {}
    
    
    Blocks.append(entities.Block(bId, Type, coords[0], coords[1], width, height, title, description, additionalFields ))
    DiagramToBlock.append((dId, bId))
    return bId

def addLink(content):
    keys = content.keys()
    Type = content["Type"] if "Type" in keys else None
    sId = content["sId"] if "sId" in keys else None
    tId = content["tId"] if "tId" in keys else None
    try:
        dId = int(content["dId"]) if "dId" in keys else None
    except ValueError:
        return None
    if Type is None or sId is None or tId is None or dId is None or not (dId,tId) in DiagramToBlock or not (dId,sId) in DiagramToBlock:
        return None 
    lId = len(Links)
    Links.append(entities.Link(lId, Type, sId, tId))
    DiagramToLink.append((dId, lId))
    return lId