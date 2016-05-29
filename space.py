import time
class Space(object):

    def __init__(self, x, y, rangex, rangey):     
        self.current = x, y
        self.action = ['walk', 'investigate', 'take', 'leave', 'actions']
        self.directions = {'north', 'east', 'south', 'west',
                           'northeast', 'northwest', 'southeast', 'southwest',
                           'n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw'}

        self.grid = {}
        self.rangex, self.rangey = rangex, rangey
        for x in range(1, self.rangex+1):
            for y in range(1, self.rangey+1):
                self.grid[(x, y)] = None

        self.thing = None

    def actions(self, action, human, room = None):
        self.human = human
        self.room = None
        action = action.split(" ")
        for i in action:
            if i in self.action:
                if i == 'walk':
                    action.remove("walk")
                    if len(action) > 0:
                        a = self.walk(action)
                        return a
                    else:
                        print('\nSimon says: "Consider walking in a direction."')
                        return True

                if i == 'investigate':
                    action.remove('investigate')
                    if len(action) > 0:
                        a = self.investigate(action)
                        return a
                    else:
                        print('\nSimon says: "Investigate what, exactly?"')
                        return True

                if i == "take":
                    if self.thing == None:
                        print('\nSimon says: "There is nothing to take here."')
                        return True
                    else:
                        self.take()
                        return False

                if i == "leave":
                    print('\nYou leave it be.')
                    return False

                if i == 'actions':
                    print('\nSimon says: "The actions you can take are: {0}."'.format(", ".join(self.action)))
                        
            else: print('\nSimon says: "I do not know what you mean by "{0}"".'.format(i))
            
    def walk(self, directions):
        for i in directions:
            if i in self.directions:
                if ("north" in i or i == "n" or i == 'nw' or i == 'ne') and self.current[1] == 1:
                    self.nothing()
                elif ("south" in i or i == "s" or i == 'sw' or i == 'se') and self.current[1] == self.rangey:
                    self.nothing()
                elif ("west" in i or i == "w" or i == 'nw' or i == 'sw') and self.current[0] == 1:
                    self.nothing()
                elif ("east" in i or i == "e" or i == 'ne' or i == 'se') and self.current[0] == self.rangex:
                    self.nothing()
                elif i == "north" or i == "n":
                    self.current = self.current[0], self.current[1] - 1
                    return False
                elif i == "south" or i == "s":
                    self.current = self.current[0], self.current[1] + 1
                    return False
                elif i == "west" or i == "w":
                    self.current = self.current[0] - 1, self.current[1]
                    return False
                elif i == "east" or i == "e":
                    self.current = self.current[0] + 1, self.current[1]
                    return False
                elif i == "northwest" or i == "nw":     
                    self.current = self.current[0] - 1, self.current[1] - 1
                    return False
                elif i == "northeast" or i == "ne":
                    self.current = self.current[0] + 1, self.current[1] - 1
                    return False
                elif i == "southwest" or i == "sw":
                    self.current = self.current[0] - 1, self.current[1] + 1
                    return False
                elif i == "southeast" or i == "se":
                    self.current = self.current[0] + 1, self.current[1] + 1
                    return False
            else:
                print('\nSimon says: "Try another direction."')
                return True

    def nothing(self):
        print('\nSimon says: "There is nothing out there."')
        return True

    def investigate(self, space):
        current = self.grid[(self.current[0], self.current[1])]
        if space[0] == current.kind:
            print("\nYou investigate the {0}.".format(space[0]))

            if len(current.things) == 0:
                print("\nThere is nothing here.")
                return True

            else:
                #One objects per space
                thing = current.things[0]
                print("\nThere is a {0} here!".format(thing.longkind))
                tl = input('Simon says: "You going to take or leave that?"\naction: ')

                if tl == 'take':
                    self.thing = thing
                    a = self.actions(tl, self.human)
                    return a
                
                self.actions(tl, self.human)
                return False
            
        for i in self.human.inventory:
            if space[0] == i.kind:
                print("\n" + i.description)
                return False
            
        print('\nSimon says: "There is no {0} to investigate here."'.format(space[0]))
        return True

    def take(self):
        if self.room:
            self.thing.room = room
        self.human.inventory.append(self.thing)
        print("\nYou take the {0}.".format(self.thing.kind))
        self.grid[(self.current[0], self.current[1])].things = []
        self.thing = None

    def describe_space(self):
        
        x = self.current[0]
        y = self.current[1]

        q = {}
        d = ['north',
             'west', 'east',
             'south']
        d2 = [[x, y-1],
              [x-1, y], [x+1, y],
              [x, y+1]]

        for i in zip(d, d2):
            try:
                q[i[0]] = self.grid[(i[1][0], i[1][1])]
            except KeyError:
                q[i[0]] = None

        s = ""
        for i in q.keys():
            if q[i] != None:
                s += "\nThere is a {0} {1} to the {2}.".format(q[i].adjective, q[i].kind, i)

        print("{0}".format(s))

        time.sleep(1)
                
        print("\nYou are standing {0} a {1} {2}.".format(self.grid[(x, y)].preposition,
                                                         self.grid[(x, y)].adjective,
                                                         self.grid[(x, y)].kind))
        time.sleep(1)
        if self.grid[(x, y)].description != None:
            print("\n" + self.grid[(x, y)].description)
