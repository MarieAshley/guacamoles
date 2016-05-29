from creature import *
from space import *
from things import *
from square import *
import time

class space1(Space):
    pass

ch1 = space1(2, 2, 3, 3)

ch1.grid[(2, 1)] = Tree(6, 5)
ch1.grid[(2, 1)].adjective = 'willow'
ch1.grid[(2, 1)].description = 'A gentle breeze causes each leaf to shimmer. It is \
peaceful here. There appears to be a hole near one of the roots. You could investigate the tree.'
ch1.grid[(2, 1)].things = [RunningShoes(ch1.grid[(2,1)].kind)]

ch1.grid[(2, 2)] = Hill(2, 2)
ch1.grid[(2, 2)].adjective = 'grassy'

ch1.grid[(2, 3)] = City(2, 3)
ch1.grid[(2, 3)].adjective = 'historic'
ch1.grid[(2, 3)].name = 'Edinburgh'
ch1.grid[(2, 3)].description = "Vibrant, beautiful, and intellectual. Your home city, Edinburgh."

ch1.describe_space()
print("There is a static noise in your pocket. You grab a walkie-talkie from your pocket...")
time.sleep(2)
print('\n? says: "My name..."')
time.sleep(1)
print('? says: "my name is Simon!"')
time.sleep(1)
human = Simon(input('Simon says: "What do you call yourself?"\nname: '))
print('Simon says: "Hello, {0}! Why are you standing? Let us walk."'.format(human.name))

while True:
    uin(ch1, human)
    ch1.describe_space()

