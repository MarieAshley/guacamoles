from creature import *
from space import *
import time, random

class space1(Space):
    pass

xrange, yrange = 5, 5
startx, starty = int(xrange/2), int(yrange/2)
ch1 = space1(startx, starty, xrange, yrange)
ch1.chapter = 1

types_of_squares = [Hill(None, None), Tree(None, None), Plain(None, None), Forest(None, None)]
special_squares = []

pu = ['You walk over to the market center, to pick up some chili. You see Pu on your way, a pretty girl your same age.',
'"Hey, you!"',
'"Yes?"',
'"Go out with me."',
'"No."',
'"I will feed you!"',
'"Okay, then. Meet me at the library at sunset."',
'Pu leaves, shaking her head.']

special = {Plain(None, None) :
               {'adjective' : 'flowery',
               'description' : 'The plain is large, bright, and makes you violently sneeze.',
               'things': Sneezewort(),
                'event' : None,
                'name': None},
           Tree(None, None) :
               {'adjective' : 'willow',
                'description': 'A gentle breeze causes each leaf to shimmer. It is \
peaceful here. There appears to be a hole near one of the roots.',
                'things': RunningShoes(),
                'event' : None,
                'name': None},
           Forest(None, None) :
               {'adjective' : 'dark',
                'description' : 'The forest is eerie and quiet. The sentient pine trees are seemingly watching you, waiting.',
                'things' : Pinecone(),
                'event' : None,
                'name' : None},
           City(None, None) :
               {'adjective' : 'historic',
                'name': 'Edinburgh',
                'description' : "Vibrant, beautiful, and intellectual. Your home city, Edinburgh.",
                'event' : pu,
                'things' : Painting()}}

for i in special.keys():
    while True:
        x, y = random.randint(1, xrange), random.randint(1,yrange)
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
            ch1.grid[(x, y)].event = special[i]['event']
            special_squares.append((x, y))
            break

for i in ch1.grid.keys():
    if ch1.grid[i] == None:
        r = random.randint(0,3)
        ch1.grid[i] = types_of_squares[r]
        ch1.grid[i].location = i[0], i[1]

ch1.describe_space(special_squares, types_of_squares)
print("\nThere is a static noise in your pocket. You grab a walkie-talkie from your pocket...")
time.sleep(2)
print('\n? says: "My name..."')
time.sleep(1)
print('? says: "my name is Simon!"')
time.sleep(1)
human = Simon(raw_input('Simon says: "What do you call yourself?"\nname: '))
human.needed_items = 3
ch1.human = human
print('Simon says: "Hello, {0}! If you are ever confused, \
try typing actions, or tips."'.format(human.name))

ch1ending = ['The sun starts to set, and casts everything in a soft orange light. {Maxwell} decides to head back to the city, and prepare for his date with Pu. He takes two steps, sneezes, and trips over a tree root. The pinecone rolls out of his pocket.'.format(Maxwell = human.name),
'His face is covered in mud. Wiping the mud from his eyes, he glares accusingly at the oak tree root and grabs the pinecone, briefly acknowledging the spirals.',
'{Maxwell} shrugs, and continues to walk back to the city. His legs are tired from a day of adventure, so he decides to sit on a nearby grassy hill. From this vantage point, he can see the green forests, grassy hills, and vast plains he was playing in earlier. With a shudder he can see the dark forest where he found the pine cone and the field of flowers. He sneezes.'.format(Maxwell = human.name),
'Irritated, he aggressively grabs the smashed up sneezewort from his pocket, and purposefully aims the next violent sneeze at the bunch of flowers. {Maxwell} regretfully inspects the snot covered petals, these were supposed to be for Pu. He drops the petals on the ground.'.format(Maxwell = human.name),
'He sees that the green stalks at the base of the flowers, where he unceremoniously ripped the flowers from the ground, systematically shoot off into more stalks, until ending at the white flowers. At the base, there is one shoot that then branches into two. A few more inches up, those two shoots branch off further, creating three total shoots. A few inches further up, those three shoots, shoot off further, creating five shoots in total, then eight, then thirteen.',
'Eight and thirteen are familiar numbers. {Maxwell} ponders if the pinecone and the sneezewort are somehow related. Are separate beings in nature, somehow related to one another?'.format(Maxwell=human.name),
'1, 1, 2, 3, 5, 8, 13.',
'1 and 1 make 2.',
'2 and 1 make 3.',
'The next number would have to be 21.',
'It is night now, and {Maxwell} is still on the grassy hill, lost in thought, and running late for his date with Pu. In a panic, he realizes that he has nothing to give her! He starts running back to the city. He twists an ankle in a small sink hole and tumbles down the hill. Stunned, he rolls over and stares up at the night sky.'.format(Maxwell = human.name),
'A white streak spans overhead. {Maxwell} thinks back to the painting of the Whirlpool Galaxy, by Rosse. The spirals are so peaceful, harmonious even. It looks like a sea shell. Small in the beginning, and spiraling out bigger and bigger, but again in a systematic way.'.format(Maxwell=human.name),
'Was the Earth and nature related to something much bigger, the Universe?',
'Shoot! His date. Sprinting now, {Maxwell} finally makes it back to the city. He finds Pu by the library. Out of breath, embarrassed, he apologizes. Pu just watches him with an amused look on her heart shaped faced, her blue eyes peering into his soul.'.format(Maxwell=human.name),
'"Looks like you just went on an adventure."',
'"Heh, I really did. I have something to show you." {Maxwell} leads her into the library, into a section that has a display of ordinary seashells.'.format(Maxwell=human.name),
'"Look at these shells." said {Maxwell}.'.format(Maxwell=human.name),
'"I see them, they are so handsome. Look how they sparkle!"',
'"Yeah..." mutters {Maxwell}, briefly wondering if he should wear sea shells so that Pu would find him handsome. No... that idea was stupid. "Right, remember their pattern."'.format(Maxwell=human.name),
'{Maxwell} takes the painting of the Whirlpool Galaxy from his pocket and handed it to Pu.'.format(Maxwell=human.name),
'"More sparkles!" exclaimed Pu.',
'"More spirals." offered {Maxwell}.'.format(Maxwell=human.name),
'{Maxwell} leads Pu outside of the library and out of the city a few steps, until the glare from the candle lights dimmed enough so they can view the night sky unobstructed.'.format(Maxwell=human.name),
'"See the white streak across the sky?" ruminated {Maxwell}.'.format(Maxwell=human.name),
'"Yes."',
'"Remember the painting, and the seashells?"',
'"Yes."',
'"I think we are in one of those galaxies, Pu. I think that white streak is one of the arms and that those arms in the spiral are related to the seashell. And furthermore, I think that relationship extends to pinecones, flowers, and hundreds if not thousands of things on earth. I think that what defines the heavens, also defines the smallest and seemingly most insignificant items on earth."',
'"Everything is made using the same recipe?"',
'"There are probably many recipes, but everything may be made from the same cookbook."',
'"Well, that just proves what I have thought all along."',
'"God?"',
'"Leave him out of this, respectfully. Regardless of what we believe, if this is true, if there is a universal relationship that can be defined, observed, and proven, it shows us at least one thing."',
'"What is that, Pu?"',
'"We should be able to look at everything and say \'I can relate to you.\'"',
'Both of them stared up into the night sky, thoughts disrupted by two grumbling stomachs.',
'"You promised me dinner, {Maxwell}. I wanted to try guacamole."'.format(Maxwell=human.name),
'"Where are the guacamoles?"',
'Pu smiled at {Maxwell}. For being such a bright kid, with such a special mind, he could say some silly things.'.format(Maxwell=human.name),
'"I am not sure. Surely, we can find an avocado or two somewhere in the city." Pu took {Maxwell}\'s hand and led him back into the city.'.format(Maxwell=human.name)]

while True:
    w = True
    while w:
        w = ch1.actions(raw_input('action: '))
    ch1.describe_space(special_squares, types_of_squares)
    if ch1.human.needed_items == 0:
        raw_input('Simon says: "Press enter when you have finished reading."\n')
        for i in ch1ending:
            raw_input(i + "\n")
        print("\nThe End")
        break
