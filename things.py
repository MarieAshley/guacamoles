from creature import *

class Pinecone(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'pinecone'

class RunningShoes(Inventory):

    def __init__(self, room):
        Inventory.__init__(self, room)
        self.kind = 'pair of running shoes'
        
