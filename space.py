class Space(object):

    def __init__(self, x, y):     
        self.current = x, y
        self.action = {'walk'}
        self.directions = {'north', 'east', 'south', 'west',
                           'northeast', 'northwest', 'southeast', 'southwest',
                           'n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw'}

        self.grid = {}
        for x in range(1, 12):
            for y in range(1, 12):
                self.grid[(x, y)] = None

    def actions(self, action):       
        action = action.split(" ")
        for i in action:
            if i in self.action:
                if i == 'walk':
                    action.remove("walk")
                    if len(action) > 0:
                        self.walk(action)
                        return False
                    else:
                        print('Simon says: "Consider walking in a direction."')
                        return True
            else: print('Simon says: "I do not know what you mean by "{0}"".'.format(i))
            
    def walk(self, directions):
        for i in directions:
            if i in self.directions:
                if i == "north":
                    self.current = self.current[0], self.current[1] - 1
            else: print('Simon says: "Try another direction."')

    def describe_space(self):
        
        x = self.current[0]
        y = self.current[1]

        q = {'north west': None,
             'north': self.grid[(x, y -1)],
             'north east': None,
             'west': None,
             'east': None,
             'south west': None,
             'south': None,
             'south east': None}

        s = ""
        for i in q.keys():
            if q[i] != None:
                s += "There is a {0} {1} to the {2}.".format(q[i].description, q[i].kind, i)
                
        print("\nYou are standing on a {0} {1}.".format(self.grid[(x, y)].description, self.grid[(x, y)].kind))
        print("\n{0}".format(s))
        

class Square(object):

    def __init__(self, x, y):
        self.location = x, y
        self.kind = None
        self.description = None

class Hill(Square):
    pass

class Tree(Square):
    pass
