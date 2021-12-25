class Project():
    def __init__(self, pId, name, description):
        self.Id = pId
        self.name = name
        self.description = description
    def serialize(self):
        return vars(self)
        

class Diagram():
    def __init__(self, dId, name, description,Type,mode, blocks=[], links = []):
        self.Id = dId
        self.name = name
        self.description = description        
        self.Type = Type
        self.mode = mode
        self.blocks = blocks.copy()
        self.links = links.copy()
        
    def serializeInfo(self):
        res = {}
        for key in vars(self).keys():
            if key != 'blocks' and key != "links":
                res[key] = self.__dict__[key]
        return res 
    def serializeContent(self):
        res = {}
        res["blocks"] = [block.serialize() for block in self.blocks]
        res["links"] = [links.serialize() for links in self.links]
        return res 

    def serializeWhole(self):
        res = self.serializeContent() 
        res.update(self.serializeInfo())
        return res


'''

{
    Id : Id,
    ...
    additionalFields : {
            "methods" : [],
            ""
        }

}

'''
# TODO maybe its a good idea to have different types of blocks and 
# inherit from this class
class Block():
    def __init__(self, bId, Type, x, y, width, height, title="", description="", additionalFields={}):
        self.Id= bId
        self.Type = Type
        self.coords = (x,y)
        self.width = width
        self.height = height
        self.title = title
        self.description = description
        self.additionalFields = additionalFields
    def serialize(self):
        return vars(self)

class Link():
    def __init__(self, lId, Type, sourceId, targetId):
        self.Id = lId
        self.Type = Type
        self.sId = sourceId
        self.tId = targetId
    def serialize(self):
        return vars(self)

