class Simon(object):
    def __init__(self, name):
        "Initialize Simon"
        self.name = name
        self.age = 11
        self.curious = True
        self.inventory = []
        self.needed_items = None
        
class Inventory(object):
    
    def __init__(self):
        self.kind = None
        self.longkind = None
        self.description = None
        self.name = None
        self.subtract_from_needed_items = 0

class Pinecone(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'pinecone'
        self.longkind = 'forest full of scaly pinecones'
        self.description = "You turn the pinecone upside down and notice spirals.  There are two sets of spirals on the pinecone. Tracing with your finger, you count eight spirals going clockwise and thirteen spirals going counter clockwise."
        self.trigger = True
        self.subtract_from_needed_items = 1

        self.desc2 = "pine cone desc2 test"

class RunningShoes(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'shoes'
        self.longkind = 'pair of running shoes'
        self.description = "At least you think these are running shoes. \
They look more like a pair of dress shoes, but with two spikes near the toes and heals. They are a perfect fit, not at all uncomfortable. You feel springy."
        self.trigger = True

        self.desc2 = "shoes desc2 test"

        
class Sneezewort(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'sneezewort'
        self.longkind = 'field of flowers, which you know as sneezewort,'
        self.description = "White flowers that appear to be the cause of your sneezing."
        self.trigger = True
        self.subtract_from_needed_items = 1

        self.desc2 = "sneezewort desc2 test"

class Painting(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'painting'
        self.longkind = 'painting of the Milky Way'
        self.description = "The painting is a small representation of the Whirpool Galaxy, drawn by William Parsons, 3rd Earl of Rosse. The original drawing was created this year, 1845. A description next to the small painting mentions that Rosse studied this galaxy using the Leviathan of Parsontown telescope."
        #Fall asleep and discover each pattern. Transported through time, through the painting.
        self.trigger = True
        self.subtract_from_needed_items = 1

        self.desc2 = "paining desc2 test"

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

    
