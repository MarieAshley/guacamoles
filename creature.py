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

def take(human, thing, room = None):
    if room:
        thing.room = room
    human.inventory.append(thing)
    print("You take the {0}.".format(thing.kind))

def uin(ch, human = None, room = None):
    w = True
    while w:
        w = ch.actions(input('action: '))
        if isinstance(w, Inventory):
            take(human, w, room)
            break
    
