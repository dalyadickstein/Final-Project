import platform
import os
import sys

from random import randint
from tools import (
  STAT_OPTIONS, pick_stats, pick_element, pick_moveset, print_move
)
from moves import FIRE_MOVELIST, Move, Fireball, Inferno
from elementalist import Elementalist
from net import (
  start_client_and_connect_to_server,
  start_server_and_connect_to_client,
  send, receive
)

# adapted from gist.github.com/ssbarnea/1316877
def supports_ansi():
  stdout_is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
  term_is_ansi = 'TERM' in os.environ and os.environ['TERM'] == 'ANSI'
  if not stdout_is_a_tty and not term_is_ansi:
    return False
  if platform.system() == 'Windows' and not term_is_ansi:
    return False
  return True


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
  if supports_ansi():
    print('\x1b[3F\x1b[J', end='') # clear initial connection text
  else:
    print()

  server_element = pick_element()

  # given the number stat chosen, get the map for those stats
  server_stat_num = int(pick_stats()) - 1
  server_stats = STAT_OPTIONS[server_stat_num]

  # pick moveset from that elementalist's movelist of possible moves
  if server_element == 'earth':
    server_moveset = pick_moveset(EARTH_MOVELIST)
  elif server_element == 'fire':
    server_moveset = pick_moveset(FIRE_MOVELIST)
  elif server_element == 'water':
    server_moveset = pick_moveset(WATER_MOVELIST)
  elif server_element == 'wind':
    server_moveset = pick_moveset(WIND_MOVELIST)

  server_elementalist = Elementalist(
    server_element, server_stats['hp'], server_stats['attack'], 
    server_stats['speed'], server_moveset
  )

  client_info = receive(client)
  # don't trust client: check info before instantiating elementalist
  if (
    client_info['element'] != 'earth' and client_info['element'] != 'fire' and
    client_info['element'] != 'water' and client_info['element'] != 'wind'
  ):
    raise SystemExit('The client\'s element was invalid. Client may be ' + 
      'tampering with the code. Exiting the program.'
    )
  # check that client chose one of the five stats options
  if client_info['stats'] not in range (1, 6):
    raise SystemExit('The client\'s stats choice was invalid. Client may be ' +
      'tampering with the code. Exiting the program.'
    )
  # check that the moveset is valid
  for choice in client_info['moveset']:
    # check that choice matches the name of a move in the proper movelist
    valid_choice = False
    if client_info['element'] == 'earth':
      for move in EARTH_MOVELIST:
        if choice == move.name:
          valid_choice = True
    if client_info['element'] == 'fire':
      for move in FIRE_MOVELIST:
        if choice == move.name:
          valid_choice = True
    if client_info['element'] == 'water':
      for move in WATER_MOVELIST:
        if choice == move.name:
          valid_choice = True
    if client_info['element'] == 'wind':
      for move in WIND_MOVELIST:
        if choice == move.name:
          valid_choice = True
    # if one of the moves was not in the proper movelist
    if not valid_choice:
      raise SystemExit('The client\'s move choice was invalid. Client may be ' +
        'tampering with the code. Exiting the program.'
      ) 
  # finished checking client_info

  # Given the number stat chosen, get the map for those stats
  client_stat_num = int(client_info['stats']) - 1
  client_stats = STAT_OPTIONS[client_stat_num]

  client_elementalist = Elementalist(
    client_info['element'], client_stats['hp'], client_stats['attack'],
    client_stats['speed'], client_info['moveset']
  )

  print('Let the battle commence!')

  # battle until one dies
  while True:
    for move in server_elementalist.moveset:
      print_move(move)
    while True: 
      move_name = input('Choose your move: ').lower()
      if move_name in server_elementalist.moveset:
        break
    # find what move the user's string refers to and call it move_choice
    for move in server_elementalist.movelist:
      if move.name == move_name:
        move_choice = move
        break

    send and receive

  # my_name = input('Hey there, what\'s your name? ')
  # friend_name = receive(client)
  # send(client, my_name)
  # print('Hi {}, I\'m {}.'.format(my_name, friend_name))

def play_as_client(server):
  if supports_ansi():
    print('\x1b[3F\x1b[J', end='') # clear initial connection text
  else:
    print()

  client_element = pick_element()
  client_stats = pick_stats()
  # pick moveset from that elementalist's movelist of possible moves
  if client_element == 'earth':
    client_moveset = pick_moveset(EARTH_MOVELIST)
  elif client_element == 'fire':
    client_moveset = pick_moveset(FIRE_MOVELIST)
  elif client_element == 'water':
    client_moveset = pick_moveset(WATER_MOVELIST)
  elif client_element == 'wind':
    client_moveset = pick_moveset(WIND_MOVELIST)

  client_info = {
    'element': client_element
    'stats': client_stats
    'moveset': client_moveset
  }
  send(server, client_info)

  # my_name = input('Hey there, what\'s your name? ')
  # send(server, my_name)
  # friend_name = receive(server)
  # print('Hi {}, I\'m {}.'.format(my_name, friend_name))

if __name__ == '__main__':
  if 'start' in input('Would you like to start or join? ').lower():
    with start_server_and_connect_to_client() as client:
      play_as_server(client)
  else:
    with start_client_and_connect_to_server() as server:
      play_as_client(server)
