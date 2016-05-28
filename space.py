import time
class Space(object):

    def __init__(self, x, y, rangex, rangey):     
        self.current = x, y
        self.action = {'walk', 'investigate', 'take', 'leave'}
        self.directions = {'north', 'east', 'south', 'west',
                           'northeast', 'northwest', 'southeast', 'southwest',
                           'n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw'}

        self.grid = {}
        self.rangex, self.rangey = rangex, rangey
        for x in range(1, self.rangex+1):
            for y in range(1, self.rangey+1):
                self.grid[(x, y)] = None

    def actions(self, action, thing = None):       
        action = action.split(" ")
        for i in action:
            if i in self.action:
                if i == 'walk':
                    action.remove("walk")
                    if len(action) > 0:
                        a = self.walk(action)
                        return a
                    else:
                        print('Simon says: "Consider walking in a direction."')
                        return True

                if i == 'investigate':
                    action.remove('investigate')
                    if len(action) > 0:
                        a = self.investigate(action)
                        return a
                    else:
                        print('Simon says: "Investigate what, exactly?"')
                        return True

                if i == "take":
                    if thing == None:
                        print('Simon says: "There is nothing to take here."')
                        return True
                    else:
                        return thing
                        
            else: print('Simon says: "I do not know what you mean by "{0}"".'.format(i))
            
    def walk(self, directions):
        for i in directions:
            if i in self.directions:
                if i == "north":
                    self.current = self.current[0], self.current[1] - 1
                    return False
            else:
                print('Simon says: "Try another direction."')
                return True

    def investigate(self, space):
        current = self.grid[(self.current[0], self.current[1])]
        if space[0] == current.kind:
            print("You investigate the {0}.".format(space[0]))

            if len(current.things) == 0:
                print("There is nothing here.")
                return True

            else:
                #One objects per space
                thing = current.things[0]
                print("There is a {0} here!".format(thing.kind))
                a = self.actions(input("Simon here: You going to take or leave that?\naction: "), thing = thing)
                return a
        else:
            print("There is no {0} to investigate here.".format(space[0]))
            return True

    def describe_space(self):
        
        x = self.current[0]
        y = self.current[1]

        q = {}
        d = ['north west', 'north', 'north east',
             'west', 'east',
             'south west', 'south', 'south east']
        d2 = [[x-1, y-1],[x, y-1], [x+1, y-1],
              [x-1, y], [x+1, y],
              [x-1, y+1], [x, y+1], [x+1, y+1]]

        for i in zip(d, d2):
            try:
                q[i[0]] = self.grid[(i[1][0], i[1][1])]
            except KeyError:
                q[i[0]] = None

        s = ""
        for i in q.keys():
            if q[i] != None:
                s += "There is a {0} {1} to the {2}.".format(q[i].adjective, q[i].kind, i)

        print("{0}\n".format(s))

        time.sleep(1)
                
        print("You are standing {0} a {1} {2}.\n".format(self.grid[(x, y)].preposition,
                                                         self.grid[(x, y)].adjective,
                                                         self.grid[(x, y)].kind))
        time.sleep(1)
        if self.grid[(x, y)].description != None:
            print(self.grid[(x, y)].description + "\n")
        

class Square(object):

    def __init__(self, x, y):
        self.location = x, y
        self.kind = None
        self.preposition = None
        self.adjective = None
        self.description = None
        self.things = []

class Hill(Square):

    def __init__(self, x, y):
        Square.__init__(self, x, y)
        self.kind = "hill"
        self.preposition = "on"

class Tree(Square):

    def __init__(self, x, y):
        Square.__init__(self, x, y)
        self.kind = "tree"
        self.preposition = "under"
