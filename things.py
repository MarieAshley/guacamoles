from creature import *

class Pinecone(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'pinecone'
        self.longkind = 'forest full of scaly pinecones'
        self.description = "The scales on the pinecone are facinating."

class RunningShoes(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'shoes'
        self.longkind = 'pair of running shoes'
        self.description = "At least you think these are running shoes. They look more like a pair of dress shoes, but with two spikes near the toes and heals. They are a perfect fit, not at all uncomfortable. You feel springy."
        
class Sneezewort(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'sneezewort'
        self.longkind = 'field of flowers, which you know as sneezewort,'
        self.description = "White flowers that appear to be the cause of your sneezing."

class Painting(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'painting'
        self.longkind = 'painting of the Milky Way'
        self.description = "The painter had a strange attention to detail. You feel as if you could just fall into the painting."
        #Fall asleep and discover each pattern. Transported through time, through the painting.
