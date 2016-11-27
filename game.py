import sys

from random import randint

from net import (
  start_client_and_connect_to_server,
  start_server_and_connect_to_client,
  send, receive
)

class Elementalist(object):

  def __init__(self, element):
    self.element = element
    self.hp = 200
    self.KOd = False

  def attack(self, other): # must pass in self?
    damage = randint(0, 50)
    print('Did {} damage!'.format(damage))
    other.hp -= damage
    if other.hp <= 0:
      print('KO\'d!!! You defeated your opponent!')
      other.KOd = True


# if __name__ == '__main__':
#   element1 = input('Player 1: Choose an element: ')
#   element2 = input('Player 2: Choose an element: ')
#   elementalist1 = Elementalist(element1)
#   elementalist2 = Elementalist(element2)
#   while True:
#     move = input('Player 1: Choose your move: ')
#     if move.lower() == 'attack':
#       elementalist1.attack(elementalist2)
#     if elementalist2.KOd:
#       break
#     move = input('Player 2: Choose your move: ')
#     if move.lower() == 'attack':
#       elementalist2.attack(elementalist1)
#     if elementalist1.KOd:
#       break

def play_as_server(client):
  print('\x1b[3F\x1b[J', end='') # clear initial connection text
  my_name = input('Hey there, what\'s your name? ')
  friend_name = receive(client)
  send(client, my_name)
  print('Hi {}, I\'m {}.'.format(my_name, friend_name))

def play_as_client(server):
  print('\x1b[3F\x1b[J', end='') # clear initial connection text
  my_name = input('Hey there, what\'s your name? ')
  send(server, my_name)
  friend_name = receive(server)
  print('Hi {}, I\'m {}.'.format(my_name, friend_name))

if __name__ == '__main__':
  if ('start' in input('would you like to start or join? ').lower()):
    with start_server_and_connect_to_client() as client:
      play_as_server(client)
  else:
    with start_client_and_connect_to_server() as server:
      play_as_client(server)
