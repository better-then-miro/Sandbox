from app import entities
import copy


Projects = [
    entities.Project(0, "test 0","Project 0" ),
    entities.Project(1, "test 1","Project 1" ),
    entities.Project(2, "test 2","Project 2" )
]

Diagrams = [
    entities.Diagram(0, "Diagram 0", "-","Type"),
    entities.Diagram(1, "Diagram 1", "-","Type"),
    entities.Diagram(2, "Diagram 2", "-","Type"),
    entities.Diagram(3, "Diagram 3", "-","Type")
] 

Blocks = [
    entities.Block(0,"Std",0,0,5,5),
    entities.Block(1,"Std",10,10,5,5),
    entities.Block(2,"Std",0,0,5,5),
    entities.Block(3,"Std",10,10,5,5),
]

Links = [
    entities.Link(0,"Std", 0,1),
    entities.Link(1,"Std", 3,2)
]


DiagramToBlock = [
    (0,0),
    (0,1),
    (1,2),
    (1,3)
]

DiagramToLink = [
    (0,0),
    (1,1)
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
    if pId > len(Projects) or pId < 0:
        return None 
    return [Diagrams[dId] for (ppId,dId) in ProjectToDiagrams if ppId==pId]

def getDiagramContentByDID(dId):
    if dId > len(Diagrams) or dId < 0:
        return None
    dia = copy.copy(Diagrams[dId])
    dia.blocks = [Blocks[bId] for (ddId, bId) in DiagramToBlock if ddId==dId]
    dia.links = [Links[lId] for (ddId, lId) in DiagramToLink if ddId==dId]
    return dia

def modifyBlockById(content):
    if content["Id"] is not None:
        bId = int( content["Id"])
        if bId > len(Blocks) or bId < 0:
            return False
        if set(content.keys()).issubset(vars(Blocks[bId])):
            for key in content.keys():
                setattr(Blocks[bId],key,content[key])
            return True
    return False

def modifyLinkById(content):
    if content["Id"] is not None:
        lId = int( content["Id"])
        if lId > len(Links) or lId < 0:
            return False
        if set(content.keys()).issubset(vars(Links[lId])):
            for key in content.keys():
                setattr(Links[lId],key,content[key])
            return True
    return False

def modifyProjectById(content):
    if content["Id"] is not None:
        pId = int( content["Id"])
        if pId > len(Projects) or pId < 0:
            return False
        if set(content.keys()).issubset(vars(Projects[pId])):
            for key in content.keys():
                setattr(Projects[pId],key,content[key])
            return True
    return False

def modifyDiagramById(content):
    if content["Id"] is not None:
        dId = int( content["Id"])
        if dId > len(Diagrams) or dId < 0:
            return False
        if set(content.keys()).issubset(vars(Diagrams[dId])):
            for key in content.keys():
                setattr(Diagrams[dId],key,content[key])
            return True
    return False