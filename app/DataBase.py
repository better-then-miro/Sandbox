import sqlite3 as sql
from sqlite3.dbapi2 import paramstyle
from entities import Block, Diagram, Project, Link
import json
from enum import Enum

class DATABASEMODE(Enum):
    MEMORY = 1
    DISK = 2


class DataBase():
    def __init__(self, mode, isInited = True, path = "", isDebug = False):
        if mode == DATABASEMODE.MEMORY:
            self.conn = sql.connect(":memory:")
            self.c = self.conn.cursor()
            self.c.execute("PRAGMA foreign_keys=on")
            self.conn.commit()
            self.__initDataBase()
            self.__debugFill()
        elif mode == DATABASEMODE.DISK:
            self.conn = sql.connect(path)
            self.c = self.conn.cursor()
            self.c.execute("PRAGMA foreign_keys=on")
            self.conn.commit()
            if not isInited:
                self.__initDataBase()
                self.__debugFill()
    
    def __initDataBase(self):
        self.c.execute('''CREATE TABLE Diagrams (    
            dId INTEGER NOT NULL,
            name TEXT,
            description TEXT,
            Type TEXT,
            mode TEXT,
            PRIMARY KEY (dId)
        )''')

        self.c.execute('''CREATE TABLE Projects (
            pId INTEGER NOT NULL,
            name TEXT,
            description TEXT,
            PRIMARY KEY (pId)
        )''')

        self.c.execute('''CREATE TABLE Blocks (
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

        self.c.execute('''CREATE TABLE Links (
            lId INTEGER NOT NULL,
            type TEXT,
            sId INTEGER,
            tId INTEGER,
            FOREIGN KEY (sId) REFERENCES Blocks (bId) ON DELETE CASCADE,
            FOREIGN KEY (tId) REFERENCES Blocks (bId) ON DELETE CASCADE,
            PRIMARY KEY (lId)
        )''')

        self.c.execute('''CREATE TABLE DiagramToBlocks (
            dId INTEGER,
            bId INTEGER,
            FOREIGN KEY (dId) REFERENCES Diagrams (dId) ON DELETE CASCADE,
            FOREIGN KEY (bId) REFERENCES Blocks (bId) ON DELETE CASCADE
        )
        ''')

        self.c.execute('''CREATE TABLE ProjectToDiagrams (
            pId INTEGER,
            dId INTEGER,
            FOREIGN KEY (pId) REFERENCES Projects (pId) ON DELETE CASCADE,
            FOREIGN KEY (dId) REFERENCES Diagrams (dId) ON DELETE CASCADE
        )
        ''')

        self.c.execute('''CREATE TABLE DiagramToLinks (
            dId INTEGER,
            lId INTEGER,
            FOREIGN KEY (dId) REFERENCES Diagrams (dId),
            FOREIGN KEY (lId) REFERENCES Links (lId) ON DELETE CASCADE
        )
        ''')

        self.conn.commit()

    def __debugFill(self):
        pr1 = Project(None, "pr1", "pr1")
        pr2 = Project(None, "pr2", "pr2")
        self.addNewProject(pr1)
        self.addNewProject(pr2)

        dia1 = Diagram(None, "dia1", "descp1", "Type1","mode1")
        dia2 = Diagram(None, "dia2", "descp2", "Type2","mode2")
        self.addNewDiagram(dia1,pr1.Id)
        self.addNewDiagram(dia2,pr2.Id)

        bl1 = Block(None, "Type1", 1,1,10,10)
        bl2 = Block(None, "Type2", 2,2,20,20)
        bl3 = Block(None, "Type3", 3,3,30,30)
        bl4 = Block(None, "Type4", 4,4,40,40)


        self.addNewBlock(bl1,dia1.Id)
        self.addNewBlock(bl2,dia1.Id)
        self.addNewBlock(bl3,dia2.Id)
        self.addNewBlock(bl4,dia2.Id)

        l1 = Link(None, "Type1", bl1.Id, bl2.Id)
        l2 = Link(None, "Type1", bl2.Id, bl1.Id)
        l3 = Link(None, "Type1", bl4.Id, bl3.Id)

        self.addNewLink(l1, dia1.Id)
        self.addNewLink(l2, dia1.Id)
        self.addNewLink(l3, dia2.Id)


    def addNewProject(self, pr):
        with self.conn:
            self.c.execute("INSERT INTO Projects VALUES (NULL, :name, :description)", {"name":pr.name, "description": pr.description})
        pr.Id = self.c.lastrowid
        return pr.Id 

    def addNewDiagram(self,dia, pId):
        with self.conn:
            self.c.execute("INSERT INTO Diagrams VALUES (NULL, :name, :description, :type, :mode)", 
            {"name":dia.name, "description": dia.description, "type":dia.Type, "mode":dia.mode})
            
            key = self.c.lastrowid
            self.c.execute("INSERT INTO ProjectToDiagrams VALUES (:pId, :dId)", {"pId":pId, "dId": key})
        dia.Id = key
        return dia.Id

    def addNewBlock(self,block,dId):
        params = block.serialize()
        params["x"]=block.coords[0]
        params["y"]=block.coords[1]
        params.pop("coords")
        params.pop("Id")
        params["additionalFields"] = json.dumps(block.additionalFields)
        with self.conn:
            self.c.execute('''INSERT INTO Blocks VALUES (NULL, :Type, :x, :y, :width, :height, :description, :title, :additionalFields)''', params)
            block.Id = self.c.lastrowid
            self.c.execute("INSERT INTO DiagramToBlocks VALUES (:dId, :bId)", {"dId":dId, "bId":block.Id})
        return block.Id

    def addNewLink(self,link,dId):
        params = link.serialize()
        params.pop("Id")
        with self.conn:
            self.c.execute("INSERT INTO Links VALUES (NULL, :Type, :sId, :tId)",params)
            link.Id = self.c.lastrowid
            self.c.execute("INSERT INTO DiagramToLinks VALUES (:dId, :lId)", {"dId":dId, "lId":link.Id})
        return link.Id


    def getDiagrams(self, pId):
        with self.conn:
            self.c.execute(''' SELECT d.dId, d.name, d.description, d.Type, d.mode FROM Diagrams d INNER JOIN ProjectToDiagrams pd ON
            d.dId = pd.dId and pd.pId = :pId
            ''', {"pId": pId})
            tmp = self.c.fetchall()
            res = []
            for elem in tmp:
                res.append(Diagram(elem[0],elem[1],elem[2],elem[3],elem[4]))
        return res
    
    def getDiagramsContent(self, dId):
        with self.conn:
            self.c.execute("SELECT d.dId, d.name, d.description, d.Type, d.mode FROM Diagrams d WHERE d.did = :dId", {"dId":dId})
            tmp = self.c.fetchone()
            dia = Diagram(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
            dia.blocks = self.getBlocks(dId)
            dia.links = self.getLinks(dId)
        return dia

    def getBlocks(self, dId):
        with self.conn:
            self.c.execute(''' SELECT b.bId ,b.Type ,b.x ,b.y ,b.width ,b.height ,b.description,b.title,b.additionalFields
            FROM Blocks b INNER JOIN DiagramToBlocks db ON
            b.bId = db.bId and db.dId = :dId
            ''', {"dId": dId})
            tmp = self.c.fetchall()
            res = []
            for elem in tmp:
                res.append(Block(elem[0],elem[1],elem[2],elem[3],elem[4],elem[5],elem[6],elem[7],elem[8]))
        return res

    def getLinks(self, dId):
        with self.conn:
            self.c.execute('''SELECT l.lId, l.type, l.sId, l.tId FROM Links l
            INNER JOIN DiagramToLinks dl ON 
            l.lId = dl.lId and dl.dId = :dId''', {"dId":dId})
            tmp = self.c.fetchall()
            res = []
            for elem in tmp:
                res.append(Link(elem[0],elem[1],elem[2],elem[3]))

        return res
    
    def getProjects(self):
        with self.conn:
            self.c.execute("SELECT * FROM Projects")
            tmp = self.c.fetchall()
            res = []
            for elem in tmp:
                res.append(Project(elem[0],elem[1],elem[2]))
        return res

    # ОТЛИЧНЫЙ ПЛАН, НАДЕЖНЫЙ БЛЯТЬ КАК ШВЕЙЦАРСКИЕ ЧАСЫ
    def modify(self, Table, newAttrs, Id):
        # we do need this shit because in each table the corresponding Id field 
        # starts with lowercased first letter of Table's name. dId for Diagrams, pId for Projects etc.
        if Table in ("Diagrams", "Links","Projects","Blocks"):
            idName = Table[0].lower() + "Id"
        else:
            return False 
        
        keys = newAttrs.keys()
        if "Id" in keys:
            keys.pop("Id")
        with self.conn:
            # I'm just to lazy to parse the entire json by myself. We're in python anyway
            for key in keys :
                # i dont even know whether it is an sql-injection, shitcode or smth genius
                self.c.execute("UPDATE {} SET {} = :value WHERE {} = :Id".format(Table, key,idName), {"value": newAttrs[key], "Id":Id})
        return True

    def modifyDiagram(self, newAttrs, Id):
        return self.modify("Diagrams", newAttrs, Id)

    def modifyBlock(self, newAttrs, Id):
        return self.modify("Blocks", newAttrs, Id)

    def modifyLink(self, newAttrs, Id):
        return self.modify("Links", newAttrs, Id)

    def modifyProject(self, newAttrs, Id):
        return self.modify("Projects", newAttrs, Id)


    def delete(self, Table, Id):
        if Table in ("Diagrams", "Links","Projects","Blocks"):
            idName = Table[0].lower() + "Id"
        else:
            return False
        
        with self.conn:
            self.c.execute("DELETE FROM {} WHERE {} = :Id".format(Table, idName), { "Id": Id})
        return True


    def deleteDiagram(self, Id):
        with self.conn:
            # we kinda have to do subquery cause sqlite doesn't support DELETE JOIN :self.c 
            self.c.execute(
                ''' DELETE FROM Blocks 
                    WHERE bId IN (
                        SELECT b.bId FROM Blocks b
                        INNER JOIN DiagramToBlocks db 
                        ON b.bId = db.bId and dId = :dId
                    )
                ''',
                {"dId":Id}
                )
            self.c.execute(
                ''' DELETE FROM Links 
                    WHERE lId IN (
                        SELECT l.lId FROM Links l 
                        INNER JOIN DiagramToLinks dl
                        ON l.lId = dl.lId and dl.dId = :dId
                    )
                ''',
                {"dId":Id}
            )
            self.c.execute("DELETE FROM Diagrams WHERE dId = :dId", {"dId":Id})

    def deleteBlock(self, Id):
        with self.conn:
            self.c.execute("DELETE FROM Blocks WHERE bId = :Id", {"Id": Id})
        return True

    def deleteLink(self, Id):
        with self.conn:
            self.c.execute("DELETE FROM Links WHERE lId = :Id", {"Id": Id})
        return True

    def deleteProject(self, Id):
        with self.conn:
            self.c.execute("SELECT dId FROM ProjectToDiagrams WHERE pId = :pId",{"pId":Id} )
            diagrams = self.c.fetchall()
            for dia in diagrams:
                self.deleteDiagram(dia[0])
            
            self.c.execute("DELETE FROM Projects WHERE pId = :pId", {"pId": Id})
        return True

    def debug(self):
        with self.conn:
            print("blocks")
            self.c.execute("SELECT * FROM Blocks")
            print(self.c.fetchall())
            self.c.execute("SELECT * FROM DiagramToBlocks")
            print(self.c.fetchall())
            print("links")
            self.c.execute("SELECT * FROM Links")
            print(self.c.fetchall())
            self.c.execute("SELECT * FROM DiagramToLinks")
            print(self.c.fetchall())
            print("diagrams")
            self.c.execute("SELECT * FROM Diagrams")
            print(self.c.fetchall())


db = DataBase(DATABASEMODE.MEMORY)
print(vars(db.getDiagramsContent(1).links[0]))
#print(db.getLinks(1))