from creature import *
from space import *
import time

class space1(Space):
    pass
    
ch1 = space1(6, 6)
ch1.grid[(6, 6)] = Hill(6, 6)
ch1.grid[(6, 6)].kind = "hill"
ch1.grid[(6, 6)].description = 'grassy'
ch1.grid[(6, 5)] = Tree(6, 5)
ch1.grid[(6, 5)].kind = "tree"
ch1.grid[(6, 5)].description = 'willow'
ch1.describe_space()

print("\nThere is a static noise in your pocket. You grab a walkie-talkie from your pocket...")
time.sleep(2)
print('\n? says: "My name..."')
time.sleep(2)
print('? says: "my name is Simon!"\n')
time.sleep(2)
human = Simon(input('Simon says: "Who are you?"\nname: '))
print('\n"Hello, {0}! Why are you standing?"'.format(human.name))

w = True
while w: w = ch1.actions(input('action: '))

