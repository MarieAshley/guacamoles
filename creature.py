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
        self.description = "You turn the pinecone upside down and notice two sets of spirals. Tracing with your finger, you count eight spirals going clockwise and thirteen spirals going counter clockwise."
        self.trigger = True
        self.subtract_from_needed_items = 1

        self.desc2 = ['The base of the pinecone opens! Light escapes the pinecone as the opening grows larger. Peering closer, you are thrust headfirst into another world and another time.',
'You see large mountains. There is a long meadow to the south and southeast. Beyond the meadow, there is an eleven thousand foot pass.',
'A sign shows that you are standing in Tuolumne Meadows Campground.',
'You see a kindly looking man, wearing fairly short shorts and a very casual shirt. He has thin woolen socks, and large brown hiking books. A large blue wire framed backpack rests by his feet. He dual wields a beer in one hand, and potato chips in the other.',
'Next to him, you see a girl about your age. She is dressed similar to the man standing next to her, which must be her father. A smaller green wire framed backpack rests besides her. She wields an ice cream cone.',
'They are speaking to another pair, a father and his boy scout. The father and son are sweaty, and look as if the Sierras had beaten them. His son looked to be a few years older than the little girl too, and therefore he was much stronger.',
'"Where did you come back from?” asked the kindly looking man.',
'"Donohue pass. It was brutal.” said the larger man.',
'"Oh, good. We are planning on ascending tomorrow. Anything we should watch out for?”',
'"She won’t make it.” reasoned the sweaty man.',
'The fathers looked to the little girl, who glared menacingly back at the larger man. She stared silently, but purposefully, and her look said it all, “Fuck you, dude.”',
'The father and son did not know the father and daughter. Her father has hiked to the highest mountain in the continental United States, he has gone on several backpacking trips that have lasted for days, he was a boy scout, he has run a half marathon. He is, as they say, tough and nails and extremely disciplined.',
'He also has an extremely sharp mind. He has worked for the top research facilities, has saved a research institute from sure demise, and has reported to congress. He writes amazing code, tinkers with big data, and is now obsessed with finding the question.',
'He is also very humble and would never tell you these things unless you asked. He has a few coin statements. One of his bests,',
'“Exercise the body, exercise the mind.”',
'It goes without saying that some of these traits passed down to his daughter. Humble and strong as well, she would not scream invectives. She would not even respond (another one of his daughters would feel obligated to lecture the smelly and defeated looking man). She would just show the idiot otherwise. And so they did.',
'They cleared the pass, and it was difficult. Her feet hurt, his feet hurt, but both were fueled by the assumptious statement. However, the light pair flew up, and flew down. They did not look defeated, they looked victorious. They met a large bird on the way, with claws like a velociraptor. He sized the two up, thinking, “Can I eat you?” No. He could not. They were too strong, and too fast.',
'This day forever exists as one of her father’s favorite and proudest memories of his oldest daughter.',
'You are tossed back into your world and your time, and fall hard on the ground. Dizzy, you stand back up, ready for your next adventure.']

class RunningShoes(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'shoes'
        self.longkind = 'pair of running shoes'
        self.description = "At least you think these are running shoes. \
They look more like a pair of dress shoes, but with two spikes near the toes and heals. They are a perfect fit, not at all uncomfortable. You feel springy."
        self.trigger = True

        self.desc2 = ['After placing the shoes on your feet, you hop up and sprint. You can feel the wind in your hair, and howling in your ears. Your legs move as fast as they can. You leap into the air, to see how far you can jump. You, challenging physics, have jumped too high. You close your eyes, slightly afraid at the landing to come.', 
'It never does. But you hear cheering all around you. Are they cheering for you?',
'“GO LITTLE, GO!”',
'You open your eyes. All around you, you see runners. They are wearing shoes that seem a hundred years more advanced than the ones on your feet.', 
'You look out. You’re a spectator in a cross country race! A nearby sign shows that you are at Ventura County Championships. There are two girls running, the girl in first has blond hair and pig tails. The girl in second, also has blond hair and seems graceful, determined, and strong. She is closing the gap, but the gap is still about 50 meters.', 
'A kindly guy stands next to you.', 
'“GO LITTLE TERROR, GO!”',
'Apparently not a lot of people liked the girl in first, everyone was cheering for the girl in second, save a few of the former’s friends. Pig tails had an attitude issue, and boasted that running was easy and she would win the race without any effort. Little Terror, not afraid to step on toes and usurp, aimed to dethrone the girl.', 
'25 meters to go. The kindly man is looking less kindly, and more wild. This must be his daughter.',
'Pain crosses Little Terror’s face. There is not much more she can give. They are both nearing the finish line, and with just a few seconds left in the race Little Terror breaks ahead. She wins the race!',
'There is nothing but triumphant pride on the wild man’s face. He turns to you with a huge friendly grin and jokes, “One of my daughters will save the world, the other will destroy it.”',
'You blink, and are back in your own time and in your own place.']

        
class Sneezewort(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'sneezewort'
        self.longkind = 'field of flowers, which you know as sneezewort,'
        self.description = "White flowers that appear to be the cause of your sneezing."
        self.trigger = True
        self.subtract_from_needed_items = 1

        self.desc2 = ['The flowers are pretty, and look like they would be a good gift for Pu. “Ahchoo!”',
'You wipe the snot on your sleeve and startled, realize you’re sitting in a building. There are rows of gray, huge boxes everyone. Boys are using their fingers to press down on buttons in front of them. You see the buttons in front of you too. They have letters, numbers, and even punctuation.',
'There are guys everywhere, and only a handful of girls. You see a really pretty girl, with a heart shaped face and blue eyes, sitting a few boxes away. With a jump of your heart you think it is Pu, but realize this girl is almost 10 years older than Pu. Sitting next to you, you see a kindly boy.',
'He glances a few times at the pretty girl, and obviously has a crush on her. He is working on something important, his face contorted in concentration, until he shows a large Cheshire grin.',
'The girl leaps back and laughs. There are giant lips on her computer. She looks at the man with the Cheshire grin and smiles.',
'You smile too, and look at the flowers in your hand. When you look back up, you are in your own time, and in your own place.']

class Painting(Inventory):

    def __init__(self):
        Inventory.__init__(self)
        self.kind = 'painting'
        self.longkind = 'painting of a spiral galaxy.'
        self.description = "The painting is a small representation of the Whirpool Galaxy, drawn by William Parsons, 3rd Earl of Rosse. The original drawing was created this year, 1845. A description next to the small painting mentions that Rosse studied this galaxy using the Leviathan of Parsontown telescope."
        #Fall asleep and discover each pattern. Transported through time, through the painting.
        self.trigger = True
        self.subtract_from_needed_items = 1

        self.desc2 = ["It almost looks like it could be a portal to another world."]

class Square(object):

    def __init__(self, x, y):
        self.location = x, y
        self.kind = None
        self.preposition = None
        self.adjective = None
        self.description = None
        self.things = []
        self.name = None
        self.event = None

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

    
