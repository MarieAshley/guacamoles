class Simon(object):
    def __init__(self):
        "Initialize Simon"
        self.age = 11
        self.curious = True
        self.inventory = []

# pockets, backpack, study
class Inventory(object):
    
    def __init__(self, room):
        self.room = room
        
class Pinecone(Inventory):
    pass

class Compass(Inventory):
    pass

class Book(Inventory):
    pass

def search_inventory(human):
    rooms = {}
    for i in human:
        rooms[i.room] = rooms.get(i.room, []) + [i]
    return rooms

def counter(human):
    types = {}
    for i in human:
        types[type(i).__name__] = types.get(type(i).__name__, 0) + 1
    for i in types.keys():
        print("{0}: {1}".format(i, types[i]))
