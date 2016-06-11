import time, random
class Space(object):

    def __init__(self, x, y, rangex, rangey):
        self.current = x, y
        self.action = ['walk', 'investigate', 'take', 'leave', 'actions', 'tips']
        self.directions = {'north', 'east', 'south', 'west',
                           'northeast', 'northwest', 'southeast', 'southwest',
                           'n', 'e', 's', 'w', 'ne', 'nw', 'se', 'sw'}

        self.grid = {}
        self.rangex, self.rangey = rangex, rangey
        for x in range(1, self.rangex+1):
            for y in range(1, self.rangey+1):
                self.grid[(x, y)] = None

        self.thing = None
        self.human = None

    def actions(self, action):
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
                        self.investigate(action)
                        return True
                    else:
                        print('Simon says: "Investigate what, exactly?"')
                        return True

                if i == "take":
                    if self.thing == None:
                        print('Simon says: "There is nothing to take here."')
                        return True
                    else:
                        self.take()
                        return True

                if i == "leave":
                    print('You leave it be.')
                    return True

                if i == 'actions':
                    print("\nThe actions you can take are: {0} or {1}.\n".format(", ".join(self.action[:-1]), self.action[-1]))
                    return True

                if i == 'tips':

                    L = ["We can investigate places or things, but that place or thing needs to be specified. For example, 'investigate tree' or 'investigate inventory'.",
                     "We do not need to specify the item we wish take. Just type, 'take'.",
                     "Walk in a direction. For example, type 'walk ne' or 'walk northeast'"]

                    print("\nTips:")

                    for i in L:
                        print(i + "\n")
                    return True

            else:
                print('Simon says: "I do not know what you mean by "{0}"".'.format(i))
                return True

    def walk(self, directions):
        for i in directions:
            if i in self.directions:
                if ("north" in i or i == "n" or i == 'nw' or i == 'ne') and self.current[1] == 1:
                    print('Simon says: "There is nothing out there."')
                    return True
                elif ("south" in i or i == "s" or i == 'sw' or i == 'se') and self.current[1] == self.rangey:
                    print('Simon says: "There is nothing out there."')
                    return True
                elif ("west" in i or i == "w" or i == 'nw' or i == 'sw') and self.current[0] == 1:
                    print('Simon says: "There is nothing out there."')
                    return True
                elif ("east" in i or i == "e" or i == 'ne' or i == 'se') and self.current[0] == self.rangex:
                    print('Simon says: "There is nothing out there."')
                    return True
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
                #One object per space
                thing = current.things[0]
                print("There is a {0} here!".format(thing.longkind))
                tl = raw_input('Simon says: "You going to take or leave that?"\naction: ')

                if tl == 'take':
                    self.thing = thing
                    self.actions(tl)
                    return True

                self.actions(tl)

        if space[0] == 'inventory':

            print("\nInventory:")
            self.search_inventory()
            print("")
            return True

        for n, i in enumerate(self.human.inventory):
            if space[0] == i.kind:
                print("\n" + i.description)
                if i.trigger:
                    self.human.needed_items -= i.subtract_from_needed_items
                    raw_input('Simon says: "When finished reading, press Enter."\n')
                    for i2 in i.desc2:
                        raw_input(i2 + "\n")
                    self.human.inventory[n].trigger = False
                return True

        print('Simon says: "There is no {0} to investigate here."'.format(space[0]))
        return True

    def search_inventory(self):
        rooms = {}
        for i in self.human.inventory:
            rooms[i.room] = rooms.get(i.room, []) + [i]
        print("")
        for i in rooms.keys():
            for i2 in rooms[i]:
                print(i2.kind)

    def take(self):
        self.human.inventory.append(self.thing)
        print("You take the {0}.".format(self.thing.kind))
        self.grid[(self.current[0], self.current[1])].things = []
        self.thing = None

    def describe_space(self, special_squares, types_of_squares):

        x = self.current[0]
        y = self.current[1]

        q = {}
        d = ['northwest', 'north', 'northeast',
             'west', 'east',
             'southwest', 'south', 'southeast']
        d2 = [[x-1, y-1],[x, y-1], [x+1, y-1],
              [x-1, y], [x+1, y],
              [x-1, y+1], [x, y+1], [x+1, y+1]]

        s2 = ""
        unremarkable = set()
        for i in zip(d, d2):
            try:
                q[i[0]] = self.grid[(i[1][0], i[1][1])]
                if (i[1][0], i[1][1]) in special_squares:
                    s2 += "There is a {0} {1} to the {2}.\n".format(q[i[0]].adjective, q[i[0]].kind, i[0])
                else:
                    unremarkable.add(self.grid[(i[1][0], i[1][1])])
            except KeyError:
               q[i[0]] = None

        unremarkable = list(unremarkable)
        s = "\nYou see "
        for n, i in enumerate(unremarkable):
            if len(unremarkable) == 1:
                s += "{0} {1}s.".format(i.adjective, i.kind)
            elif n == len(unremarkable) - 1:
                s += "and {0} {1}s.".format(i.adjective, i.kind)
            else:
                s += "{0} {1}s, ".format(i.adjective, i.kind)

        print(s)
        if s2 != "":
            s2 = s2[:-2]
            print(s2)

        time.sleep(1)

        print("\nYou are standing {0} a {1} {2}.".format(self.grid[(x, y)].preposition,
                                                         self.grid[(x, y)].adjective,
                                                         self.grid[(x, y)].kind))
        time.sleep(1)
        if self.grid[(x, y)].description != None:
            print(self.grid[(x, y)].description)

        if self.grid[(x,y)].event != None:
            raw_input('Simon says: "Press enter when you have finished reading."\n')
            for i in self.grid[(x,y)].event:
                raw_input(i + "\n")
            self.grid[(x,y)].event = None
