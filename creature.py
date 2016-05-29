class Simon(object):
    def __init__(self, name):
        "Initialize Simon"
        self.name = name
        self.age = 11
        self.curious = True
        self.inventory = []
        
class Inventory(object):
    
    def __init__(self, room):
        self.room = room # i.e. pocket
        self.kind = None
        self.longkind = None
        self.description = None
        self.name = None

def counter(human):
    types = {}
    for i in human:
        types[type(i).__name__] = types.get(type(i).__name__, 0) + 1
    for i in types.keys():
        print("{0}: {1}".format(i, types[i]))

def uin(ch, human, room = None):
    w = True
    while w:
        w = ch.actions(input('action: '), human, room)
    
