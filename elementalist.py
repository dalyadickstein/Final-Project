from moves import EARTH_MOVELIST, FIRE_MOVELIST, WATER_MOVELIST, WIND_MOVELIST




# from moves import FIRE_MOVELIST

# class Elementalist(object):

#     def __init__(self, element, hp, speed, power, moveset):
#         self.element = element
#         self.hp = hp
#         self.speed = speed
#         self.power = power
#         self.moveset = moveset
#         self.status = "healthy"
#         if self.element == 'fire':
#             self.movelist = FIRE_MOVELIST

#     def attack(self, move, other):
#         pass


# class OldElementalistForReferenceAndThenDeletion(object):

#   def __init__(self, element):
#     self.element = element
#     self.hp = 200
#     self.KOd = False

#   def attack(self, other): # must pass in self?
#     damage = randint(0, 50)
#     print('Did {} damage!'.format(damage))
#     other.hp -= damage
#     if other.hp <= 0:
#       print('KO\'d!!! You defeated your opponent!')
#       other.KOd = True

# class Pyromaniac(Elementalist):
#     move_list = 

#     def __init__(self, speed, power, moveset):
#         Elementalist.__init__(self, "Fire", speed, power, moveset)
    


# class Earthshaker(Elementalist):

#     def __init__(self):
#         Elementalist.__init__(self, "Ground", speed, power, moveset)

# class Aerosoldier(Elementalist):

#     def __init__(self):
#         Elementalist.__init__(self, "Air", speed, power, moveset)

# class Sealord(Elementalist):
#     def __init__(self):
#         Elementalist.__init__(self, "Water", speed, power, moveset)
