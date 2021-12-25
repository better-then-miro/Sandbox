import sqlite3 as sql
from sqlite3.dbapi2 import paramstyle
from entities import Block, Diagram, Project, Link
import json

conn = sql.connect(":memory:")

c = conn.cursor()
c.execute("PRAGMA foreign_keys=on")
conn.commit()

c.execute('''CREATE TABLE Diagrams (    
    dId INTEGER NOT NULL,
    name TEXT,
    description TEXT,
    Type TEXT,
    mode TEXT,
    PRIMARY KEY (dId)
)''')

c.execute('''CREATE TABLE Projects (
    pId INTEGER NOT NULL,
    name TEXT,
    description TEXT,
    PRIMARY KEY (pId)
)''')

c.execute('''CREATE TABLE Blocks (
    bId INTEGER NOT NULL,
    Type TEXT,
    x INTEGER,
    y INTEGER,
    width INTEGER,
    height INTEGER,
    description TEXT,
    title TEXT,
    additionalFields TEXT,
    PRIMARY KEY (bId)
)''')

c.execute('''CREATE TABLE Links (
    lId INTEGER NOT NULL,
    type TEXT,
    sId INTEGER,
    tId INTEGER,
    FOREIGN KEY (sId) REFERENCES Blocks (bId) ON DELETE CASCADE,
    FOREIGN KEY (tId) REFERENCES Blocks (bId) ON DELETE CASCADE,
    PRIMARY KEY (lId)
)''')

c.execute('''CREATE TABLE DiagramToBlocks (
    dId INTEGER,
    bId INTEGER,
    FOREIGN KEY (dId) REFERENCES Diagrams (dId) ON DELETE CASCADE,
    FOREIGN KEY (bId) REFERENCES Blocks (bId) ON DELETE CASCADE
)
''')

c.execute('''CREATE TABLE ProjectToDiagrams (
    pId INTEGER,
    dId INTEGER,
    FOREIGN KEY (pId) REFERENCES Projects (pId) ON DELETE CASCADE,
    FOREIGN KEY (dId) REFERENCES Diagrams (dId) ON DELETE CASCADE
)
''')

c.execute('''CREATE TABLE DiagramToLinks (
    dId INTEGER,
    lId INTEGER,
    FOREIGN KEY (dId) REFERENCES Diagrams (dId),
    FOREIGN KEY (lId) REFERENCES Links (lId) ON DELETE CASCADE
)
''')

conn.commit()





def addNewProject(pr):
    with conn:
        c.execute("INSERT INTO Projects VALUES (NULL, :name, :description)", {"name":pr.name, "description": pr.description})
    pr.Id = c.lastrowid
    return pr.Id 

def addNewDiagram(dia, pId):
    with conn:
        c.execute("INSERT INTO Diagrams VALUES (NULL, :name, :description, :type, :mode)", 
        {"name":dia.name, "description": dia.description, "type":dia.Type, "mode":dia.mode})
        
        key = c.lastrowid
        c.execute("INSERT INTO ProjectToDiagrams VALUES (:pId, :dId)", {"pId":pId, "dId": key})
    dia.Id = key
    return dia.Id

def addNewBlock(block,dId):
    params = block.serialize()
    params["x"]=block.coords[0]
    params["y"]=block.coords[1]
    params.pop("coords")
    params.pop("Id")
    params["additionalFields"] = json.dumps(block.additionalFields)
    with conn:
        c.execute('''INSERT INTO Blocks VALUES (NULL, :Type, :x, :y, :width, :height, :description, :title, :additionalFields)''', params)
        block.Id = c.lastrowid
        c.execute("INSERT INTO DiagramToBlocks VALUES (:dId, :bId)", {"dId":dId, "bId":block.Id})
    return block.Id

def addNewLink(link,dId):
    params = link.serialize()
    params.pop("Id")
    with conn:
        c.execute("INSERT INTO Links VALUES (NULL, :Type, :sId, :tId)",params)
        link.Id = c.lastrowid
        c.execute("INSERT INTO DiagramToLinks VALUES (:dId, :lId)", {"dId":dId, "lId":link.Id})
    return link.Id


def getDiagrams(pId):
    with conn:
        c.execute(''' SELECT d.dId, d.name, d.description, d.Type, d.mode FROM Diagrams d INNER JOIN ProjectToDiagrams pd ON
        d.dId = pd.dId and pd.pId = :pId

        ''', {"pId": pId})
        res = c.fetchall()
    return res

def getBlocks(dId):
    with conn:
        c.execute(''' SELECT b.bId ,b.Type ,b.x ,b.y ,b.width ,b.height ,b.description,b.title,b.additionalFields
         FROM Blocks b INNER JOIN DiagramToBlocks db ON
        b.bId = db.bId and db.dId = :dId
        ''', {"dId": dId})
        res = c.fetchall()
    return res

def getLinks(dId):
    with conn:
        c.execute('''SELECT * FROM Links l
        INNER JOIN DiagramToLinks dl ON 
        l.lId = dl.lId and dl.dId = :dId''', {"dId":dId})
        res = c.fetchall()
    return res

# ОТЛИЧНЫЙ ПЛАН, НАДЕЖНЫЙ БЛЯТЬ КАК ШВЕЙЦАРСКИЕ ЧАСЫ
def modify(Table, newAttrs, Id):
    # we do need this shit because in each table the corresponding Id field 
    # starts with lowercased first letter of Table's name. dId for Diagrams, pId for Projects etc.
    if Table in ("Diagrams", "Links","Projects","Blocks"):
        idName = Table[0].lower() + "Id"
    else:
        return False 
    
    keys = newAttrs.keys()
    if "Id" in keys:
        keys.pop("Id")
    with conn:
        # I'm just to lazy to parse the entire json by myself. We're in python anyway
        for key in keys :
            # i dont even know whether it is an sql-injection, shitcode or smth genius
            c.execute("UPDATE {} SET {} = :value WHERE {} = :Id".format(Table, key,idName), {"value": newAttrs[key], "Id":Id})
    return True

def modifyDiagram(newAttrs, Id):
    return modify("Diagrams", newAttrs, Id)

def modifyBlock(newAttrs, Id):
    return modify("Blocks", newAttrs, Id)

def modifyLink(newAttrs, Id):
    return modify("Links", newAttrs, Id)

def modifyProject(newAttrs, Id):
    return modify("Projects", newAttrs, Id)


def delete(Table, Id):
    if Table in ("Diagrams", "Links","Projects","Blocks"):
        idName = Table[0].lower() + "Id"
    else:
        return False
    
    with conn:
        c.execute("DELETE FROM {} WHERE {} = :Id".format(Table, idName), { "Id": Id})
    return True


def deleteDiagram(Id):
    with conn:
        # we kinda have to do subquery cause sqlite doesn't support DELETE JOIN :c 
        c.execute(
            ''' DELETE FROM Blocks 
                WHERE bId IN (
                    SELECT b.bId FROM Blocks b
                    INNER JOIN DiagramToBlocks db 
                    ON b.bId = db.bId and dId = :dId
                )
             ''',
             {"dId":Id}
            )
        c.execute(
            ''' DELETE FROM Links 
                WHERE lId IN (
                    SELECT l.lId FROM Links l 
                    INNER JOIN DiagramToLinks dl
                    ON l.lId = dl.lId and dl.dId = :dId
                )
            ''',
            {"dId":Id}
        )
        c.execute("DELETE FROM Diagrams WHERE dId = :dId", {"dId":Id})

def deleteBlock(Id):
    with conn:
        c.execute("DELETE FROM Blocks WHERE bId = :Id", {"Id": Id})
    return True

def deleteLink(Id):
    with conn:
        c.execute("DELETE FROM Links WHERE lId = :Id", {"Id": Id})
    return True

def deleteProject(Id):
    with conn:
        c.execute("SELECT dId FROM ProjectToDiagrams WHERE pId = :pId",{"pId":Id} )
        diagrams = c.fetchall()
        for dia in diagrams:
            deleteDiagram(dia[0])
        
        c.execute("DELETE FROM Projects WHERE pId = :pId", {"pId": Id})
    return True

