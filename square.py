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

    def __init__(self, x = None, y = None):
        Square.__init__(self, x, y)
        self.kind = "hill"
        self.adjective = "grassy"
        self.preposition = "on"

class Tree(Square):

    def __init__(self, x = None, y = None):
        Square.__init__(self, x, y)
        self.kind = "tree"
        self.adjective = 'large oak'
        self.preposition = "under"

class City(Square):

    def __init__(self, x = None, y = None):
        Square.__init__(self, x, y)
        self.kind = 'city'
        self.preposition = 'in'

class Plain(Square):

    def __init__(self, x = None, y = None):
        Square.__init__(self, x, y)
        self.kind = 'plain'
        self.adjective = 'vast'
        self.preposition = 'on'

class Forest(Square):

    def __init__(self, x = None, y = None):
        Square.__init__(self, x, y)
        self.kind = 'forest'
        self.adjective = 'bright green'
        self.preposition = 'in'

