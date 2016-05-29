from creature import *
from space import *
from things import *
from square import *
import time, random

class space1(Space):
    pass

ch1 = space1(2, 2, 3, 3)

types_of_squares = [Hill(None, None), Tree(None, None), Plain(None, None), Forest(None, None)]

special = {Plain(None, None) :
               {'adjective' : 'flowery',
               'description' : 'The plain is large, bright, and makes you violently sneeze.',
               'things': Sneezewort(None),
                'name': None},
           Tree(None, None) :
               {'adjective' : 'willow',
                'description': 'A gentle breeze causes each leaf to shimmer. It is \
peaceful here. There appears to be a hole near one of the roots.',
                'things': RunningShoes(None),
                'name': None},
           Forest(None, None) :
               {'adjective' : 'dark',
                'description' : 'The forest is eerie and quiet. The sentient pine trees are seemingly watching you, waiting.',
                'things' : Pinecone(None),
                'name' : None},
           City(None, None) :
               {'adjective' : 'historic',
                'name': 'Edinburgh',
                'description' : "Vibrant, beautiful, and intellectual. Your home city, Edinburgh.",
                'things' : Painting(None)}}

for i in special.keys():
    while True:
        x, y = random.randint(1, 3), random.randint(1,3)
        if ch1.grid[(x, y)] != None:
            continue
        else:
            special[i]['things'].room = ch1.grid[(x, y)]
            ch1.grid[(x, y)] = i
            ch1.grid[(x, y)].location = x, y
            ch1.grid[(x, y)].adjective = special[i]['adjective']
            ch1.grid[(x, y)].description = special[i]['description']
            ch1.grid[(x, y)].things = [special[i]['things']]
            ch1.grid[(x, y)].name = special[i]['name']
            break
            
for i in ch1.grid.keys():
    if ch1.grid[i] == None:
        r = random.randint(0,3)
        ch1.grid[i] = types_of_squares[r]
        ch1.grid[i].location = i[0], i[1]

ch1.describe_space()
print("\nThere is a static noise in your pocket. You grab a walkie-talkie from your pocket...")
time.sleep(2)
print('\n? says: "My name..."')
time.sleep(1)
print('? says: "my name is Simon!"')
time.sleep(1)
human = Simon(input('Simon says: "What do you call yourself?"\nname: '))
print('Simon says: "Hello, {0}! If you are ever confused, try typing "actions". Why are you just standing there?"'.format(human.name))

while True:
    uin(ch1, human)
    ch1.describe_space()

