from elementalist import Elementalist

class Move(object):

    def __init__(self, element, power, speed):
        self.element = element
        self.power = power
        self.speed = speed

class Fireball(Move):

    def __init__(self):
        Move.__init__(self, 'fire', 60, 50)
        self.info = 'Lobs a fireball that damages and may burn an opponent.'
        self.name = 'fireball'

    def use(user, enemy):
        # if enemy has no status condition, change of burning
        if enemy.status == 'healthy' and random.randint(3,5) % 2 == 0:
            enemy.status = 'burned'

class Inferno(Move):

    def __init__(self):
        Move.__init__(self, 'fire', 100, 10)
        self.info = (
            'Summons a raging inferno that is so powerful, the user loses HP' +
            ' out of exhaustion.'
        )
        self.name = 'inferno'

    def use(user, enemy):
        user.hp -= 15


fireball = Fireball()
inferno = Inferno()

FIRE_MOVELIST = [fireball, inferno]

    # def burns(self):
    #     return random.randint(3,5) % 2 == 0

# class Firestorm(Move):
#     def __init__(self):
#         Move.__init__('fire', 40, power)


# def fireball(user, enemy):
#     fireball = Move('fire', 50, 60)
#     fireball.info = 'Lobs a fireball that damages and may burn an opponent.'
#     if random.randint(3,5) % 2 == 0:
#         # Print out on both screens:
#         # 'Your opponent was burned!' or 'You were burned!'
#         enemy.status = 'burned'
#     enemy.hp -= fireball.power



move_list = [
    'foo',
    'bar',
    'baz'
]

fire_move_list = [
    Fireball,

]


