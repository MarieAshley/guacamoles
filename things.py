from creature import *

class Pinecone(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'pinecone'

class RunningShoes(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'shoes'
        self.longkind = 'pair of running shoes'
        self.description = "At least you think these are running shoes. They look more like a pair of dress shoes, but with two spikes near the toes and heals. They are a perfect fit, not at all uncomfortable. You feel springy."
        
