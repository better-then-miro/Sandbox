import sqlite3 as sql
from sqlite3.dbapi2 import paramstyle
from entities import Block, Diagram, Project, Link
import json

conn = sql.connect(":memory:")

c = conn.cursor()

c.execute('''CREATE TABLE Diagrams (
    dId INTEGER NOT NULL,
    name TEXT,
    description TEXT,
    Type TEXT,
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



c.execute('''CREATE TABLE DiagramToBlocks (
    dId INTEGER,
    bId INTEGER,
    FOREIGN KEY (dId)
    REFERENCES Diagrams (dId),
    FOREIGN KEY (bId)
    REFERENCES Blocks (bId)
)
''')

c.execute('''CREATE TABLE ProjectToDiagrams (
    pId INTEGER,
    dId INTEGER,
    FOREIGN KEY (pId)
    REFERENCES Projects (pId),
    FOREIGN KEY (dId)
    REFERENCES Diagrams (dId)
)
''')


conn.commit()



pr1 = Project(None, "pr1","lol")
pr2 = Project(None, "pr2","kek")

dia1 = Diagram(None, "dia1", "suka", "Type")
dia2 = Diagram(None, "dia2", "suka", "Type")
dia3 = Diagram(None, "dia3", "suka", "Type")
dia4 = Diagram(None, "dia4", "suka", "Type")
bl1 = Block(None,"Class",200,50,50,50,additionalFields={"attrs":["private static int jopa","hui"],"methods":["int main()","void lel()"]})
bl2 = Block(None,"Class",100,60,50,70)
bl3 = Block(None,"Class",300,40,100,70)
bl4 = Block(None,"Class",150,100,50,40)

def addNewProject(pr):
    with conn:
        c.execute("INSERT INTO Projects VALUES (NULL, :name, :description)", {"name":pr.name, "description": pr.description})
    pr.Id = c.lastrowid
    return pr.Id 

def addNewDiagram(dia, pId):
    with conn:
        c.execute("INSERT INTO Diagrams VALUES (NULL, :name, :description, :type)", {"name":dia.name, "description": dia.description, "type":dia.Type})
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


def getDiagrams(pId):
    with conn:
        c.execute(''' SELECT d.dId, d.name, d.description, d.Type FROM Diagrams d INNER JOIN ProjectToDiagrams pd ON
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


print("adding projects")
newId = addNewProject(pr1)
print(newId)
newId = addNewProject(pr2)
print(newId)

print("adding diagrams")
newId = addNewDiagram(dia1, pr1.Id)
print(newId)
newId = addNewDiagram(dia2, pr1.Id)
print(newId)
newId = addNewDiagram(dia3, pr2.Id)
print(newId)
newId = addNewDiagram(dia4, pr2.Id)
print(newId)
print("adding blocks")
print(addNewBlock(bl1,dia1.Id))
print(addNewBlock(bl2,dia1.Id))
print(addNewBlock(bl3,dia1.Id))
print(addNewBlock(bl4,dia2.Id))

print("now res")
print(getBlocks(dia1.Id))


conn.close()