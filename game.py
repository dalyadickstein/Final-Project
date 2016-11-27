import sys
from random import randint

class Elementalist(object):

    def __init__(self, element):
        self.element = element
        self.hp = 200
        self.KOd = False

    def attack(self, other): # must pass in self?
        damage = randint(0, 50)
        print("Did {} damage!".format(damage))
        other.hp -= damage
        if other.hp <= 0:
            print("KO'd!!! You defeated your opponent!")
            other.KOd = True


if __name__ == "__main__":
    element1 = input("Player 1: Choose an element: ")
    element2 = input("Player 2: Choose an element: ")
    elementalist1 = Elementalist(element1)
    elementalist2 = Elementalist(element2)
    while True:
        move = input("Player 1: Choose your move: ")
        if move.lower() == "attack":
            elementalist1.attack(elementalist2)
        if elementalist2.KOd:
            break
        move = input("Player 2: Choose your move: ")
        if move.lower() == "attack":
            elementalist2.attack(elementalist1)
        if elementalist1.KOd:
            break
