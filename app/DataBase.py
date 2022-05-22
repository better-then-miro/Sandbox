import sqlite3 as sql
from sqlite3.dbapi2 import paramstyle
from app import entities
import json
from enum import Enum

class DATABASEMODE(Enum):
    MEMORY = 1
    DISK = 2

class SingletonViolationException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class Singleton(type):
    __instances = {}
    def __call__(Class, *args,**kwargs):
        if Class not in Class.__instances:
            Class.__instances[Class] = super(Singleton,Class).__call__(*args, **kwargs)
        else:
            raise SingletonViolationException("Second instance of Database is not allowed")
        return Class.__instances[Class]

class DataBase(metaclass = Singleton):
    def __init__(self, mode, isInited = True, path = "", isDebug = False):
        if mode == DATABASEMODE.MEMORY:
            self.conn = sql.connect(":memory:",check_same_thread=False)
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
        pr1 = entities.Project(None, "test 0","Project 0" )
        pr2 = entities.Project(None, "test 1","Project 1" )
        pr3 = entities.Project(None, "test 2","Project 2" )
        self.addNewProject(pr1)
        self.addNewProject(pr2)
        self.addNewProject(pr3)

        dia1 = entities.Diagram(None, "Diagram 0", "-","use-case","Strict")
        dia2 = entities.Diagram(None, "Diagram 1", "-","use-case","Strict")
        dia3 = entities.Diagram(None, "Diagram 2", "-","use-case","Free")
        dia4 = entities.Diagram(None, "Diagram 3", "-","use-case","Free")
        self.addNewDiagram(dia1,pr1.Id)
        self.addNewDiagram(dia2,pr2.Id)
        self.addNewDiagram(dia3,pr3.Id)
        self.addNewDiagram(dia4,pr1.Id)

        bl1 = entities.Block(None,"Class",200,50,50,50, 'Controller', '', additionalFields=
        {
            'Attributes': ['linkType', 'sourceeLinkId', 'targetLinkId'],
            'Operations': ['AddNewBlock(blockId)', 'AddNewLink(linkId)'],
            'stereotype': ''
        })
        bl2 = entities.Block(None,"Class",100,60,50,70, 'Link', '', additionalFields=
        {
            'Attributes': ['lId', 'type', 'sourceId', 'targetId'],
            'Operations': ['AddNewBlock(blockId)', 'AddNewLink(linkId)'],
            'stereotype': ''
        })
        bl3 = entities.Block(None,"Class",300,40,100,70, additionalFields=
        {
            'Attributes': ['linkType', 'sourceeLinkId', 'targetLinkId'],
            'Operations': ['AddNewBlock(blockId)', 'AddNewLink(linkId)'],
            'stereotype': ''
        })
        bl4 = entities.Block(None,"Class",150,100,50,40, additionalFields=
        {
            'Attributes': ['linkType', 'sourceeLinkId', 'targetLinkId'],
            'Operations': ['AddNewBlock(blockId)', 'AddNewLink(linkId)'],
            'stereotype': ''
        })
        bl5 = entities.Block(None,"Use-case",100,200,60,100)
        bl6 = entities.Block(None,"Use-case",200,250,100,100)


        self.addNewBlock(bl1,dia1.Id)
        self.addNewBlock(bl2,dia1.Id)
        self.addNewBlock(bl3,dia2.Id)
        self.addNewBlock(bl4,dia2.Id)
        self.addNewBlock(bl5,dia1.Id)
        self.addNewBlock(bl6,dia1.Id)

        l1 = entities.Link(None,"Association", bl1.Id,bl2.Id)
        l2 = entities.Link(None,"Include", bl4.Id,bl3.Id)

        self.addNewLink(l1, dia1.Id)
        self.addNewLink(l2, dia2.Id)
        

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
                res.append(entities.Diagram(elem[0],elem[1],elem[2],elem[3],elem[4]))
        return res
    
    def getDiagramFromBlock(self, bId):
        with self.conn:
            self.c.execute("SELECT d.dId FROM DiagramToBlocks d WHERE d.bId = :bb", {"bb":bId})
            res = self.c.fetchone()
            if res is not None:
                res = res[0]
            return res
    def getDiagramFromLink(self, lId):
        with self.conn:
            self.c.execute("SELECT dId from DiagramToLinks WHERE lid = :l", {"l":lId})
            res = self.c.fetchone()
            if res is not None:
                res = res[0]
            return res
    
    def getDiagramsContent(self, dId):
        with self.conn:
            self.c.execute("SELECT d.dId, d.name, d.description, d.Type, d.mode FROM Diagrams d WHERE d.did = :dId", {"dId":dId})
            tmp = self.c.fetchone()
            if tmp is None:
                return None
            dia = entities.Diagram(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
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
            if tmp is None:
                return None
            res = []
            for elem in tmp:
                res.append(entities.Block(elem[0],elem[1],elem[2],elem[3],elem[4],elem[5],elem[6],elem[7], json.loads(elem[8])))
        return res

    def getLinks(self, dId):
        with self.conn:
            self.c.execute('''SELECT l.lId, l.type, l.sId, l.tId FROM Links l
            INNER JOIN DiagramToLinks dl ON 
            l.lId = dl.lId and dl.dId = :dId''', {"dId":dId})
            tmp = self.c.fetchall()
            if tmp is None:
                return None
            res = []
            for elem in tmp:
                res.append(entities.Link(elem[0],elem[1],elem[2],elem[3]))

        return res
    
    def getProjects(self):
        with self.conn:
            self.c.execute("SELECT * FROM Projects")
            tmp = self.c.fetchall()
            if tmp is None:
                return None
            res = []
            for elem in tmp:
                res.append(entities.Project(elem[0],elem[1],elem[2]))
        return res

    # ОТЛИЧНЫЙ ПЛАН, НАДЕЖНЫЙ КАК ШВЕЙЦАРСКИЕ ЧАСЫ
    def __modify(self, Table, newAttrs, Id):
        # we do need this shit because in each table the corresponding Id field 
        # starts with lowercased first letter of Table's name. dId for Diagrams, pId for Projects etc.
        if Table in ("Diagrams", "Links","Projects","Blocks"):
            idName = Table[0].lower() + "Id"
        else:
            return False 
        
        keys = newAttrs.keys()
        if "Id" in keys:
            newAttrs.pop("Id")
        with self.conn:
            # I'm just to lazy to parse the entire json by myself. We're in python anyway
            for key in keys :
                # i dont even know whether it is an sql-injection, shitcode or smth genius
                self.c.execute("UPDATE {} SET {} = :value WHERE {} = :Id".format(Table, key,idName), {"value": newAttrs[key], "Id":Id})
        return True

    def modifyDiagram(self, newAttrs, Id):
        return self.__modify("Diagrams", newAttrs, Id)

    def modifyBlock(self, newAttrs, Id):
        keys = newAttrs.keys()
        if "coords" in keys:
            newAttrs["x"]=newAttrs["coords"][0]
            newAttrs["y"]=newAttrs["coords"][1]
            newAttrs.pop("coords")
        if "additionalFields" in keys:
            newAttrs["additionalFields"] = json.dumps(newAttrs["additionalFields"])

        return self.__modify("Blocks", newAttrs, Id)

    def modifyLink(self, newAttrs, Id):
        return self.__modify("Links", newAttrs, Id)

    def modifyProject(self, newAttrs, Id):
        return self.__modify("Projects", newAttrs, Id)


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
        return True

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
            print("projects")
            self.c.execute("SELECT * FROM Projects")
            print(self.c.fetchall())
            self.c.execute("SELECT * FROM ProjectToDiagrams")
            print(self.c.fetchall())
