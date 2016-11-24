class Elementalist(object):

    def __init__(self, element, speed, power, moveset):
        self.element = element
        self.speed = speed
        self.power = power
        self.moveset = moveset

    def attack(self, other):
        pass

class Pyromaniac(Elementalist):
    move_list = 

    def __init__(self, speed, power, moveset):
        Elementalist.__init__(self, "Fire", speed, power, moveset)
    


class Earthshaker(Elementalist):

    def __init__(self):
        Elementalist.__init__(self, "Ground", speed, power, moveset)

class Aerosoldier(Elementalist):

    def __init__(self):
        Elementalist.__init__(self, "Air", speed, power, moveset)

class Sealord(Elementalist):
    def __init__(self):
        Elementalist.__init__(self, "Water", speed, power, moveset)
