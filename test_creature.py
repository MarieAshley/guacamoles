import unittest
from creature import *

adventurer = Simon()
adventurer.inventory.append(Pinecone('Pocket'))

class Test(unittest.TestCase):
    
    def test_search_inventory(self):
        self.assertIn('Pocket', search_inventory(adventurer.inventory))
        self.assertIn('Backpack', search_inventory(adventurer.inventory))
        for i in search_inventory(adventurer.inventory)['Pocket']:
            self.assertIsInstance(i, Inventory)
           
if __name__ == "__main__":
    unittest.main()
