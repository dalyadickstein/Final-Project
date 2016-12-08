class Elementalist(object):

    def __init__(self, element, hp, attack, speed, moveset):
        self.element = element
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.moveset = moveset
        self.status = "healthy"
