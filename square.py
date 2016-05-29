class Square(object):

    def __init__(self, x, y):
        self.location = x, y
        self.kind = None
        self.preposition = None
        self.adjective = None
        self.description = None
        self.things = []
        self.name = None

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

class City(Square):

    def __init__(self, x, y):
        Square.__init__(self, x, y)
        self.kind = 'city'
        self.preposition = 'in'
