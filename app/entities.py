class Project():
    def __init__(self, pId, name, description):
        self.Id = pId
        self.name = name
        self.description = description
        

class Diagram():
    def __init__(self, dId, name, description,Type, blocks=[], links = []):
        self.Id = dId
        self.name = name
        self.description = description
        self.type = Type
        self.blocks = blocks.copy()
        self.links = links.copy()


# TODO maybe its a good idea to have different types of blocks and 
# inherit from this class
class Block():
    def __init__(self, bId, Type, x,y,width, height):
        self.Id= bId
        self.Type = Type
        self.coords = (x,y)
        self.width = width
        self.height = height

class Link():
    def __init__(self, lId, Type, sourceId, targetId):
        self.Id = lId
        self.Type = Type
        self.sId = sourceId
        self.tId = targetId
        