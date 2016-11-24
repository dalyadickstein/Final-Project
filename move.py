class Move(object):

    def __init__(self, element, speed, power):
        self.element = element
        self.speed = speed
        self.power = power
        # Does the info have to be initialized, or written above, to have it?
        
    def get_info(self):
        return self.info
# make new moves: should they be their own classes?

Fireball = Move("fire", 50, 60)

class Fireball(Move):

    def __init__(self, info):
        Move.__init__("fire", 50, 60)
        self.info = "Lobs a fireball that damages and may burn an opponent."

    def burns(self):
        return random.randint(3,5) % 2 == 0

move_list = [
    "foo",
    "bar",
    "baz"
]
