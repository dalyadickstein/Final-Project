import platform
import os
import sys

from random import randint
from stats import STAT_OPTIONS
from moves import MOVES
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

def pick_stats(): 
  n = 1
  print('Next, choose which set of stats you want.')
  for stat in STAT_OPTIONS:
    print(
      'Stats {}:\nHP: {}   Attack: {}   Speed: {}\n'.format(
        n, stat['hp'], stat['attack'], stat['speed']
      )
    )
    n += 1
  while True:
    stats = input('Enter 1-5: ')
    if (
      stats == '1' or stats == '2' or stats == '3' or
      stats == '4' or stats == '5'
    ):
      return stats

def pick_element():
  element = input(
    'Elementalist! Choose your element!\nWill your spirit burn like Fire?\n' +
    'Or be both tranquil and tempestuous as Water?\nAre you as invisible and' +
    ' powerful as Wind?\nOr as unyielding as the Earth itself?\nYour element: '
  ).lower()
  while True:
    if (
      element == 'fire' or element == 'water' or 
      element == 'wind' or element == 'earth'
    ):
      return element
    element = input('Earth, Fire, Water, or Wind? ').lower()

def pick_moveset(element):
  print('Very good. It is now time to pick your moves. You may choose three:\n')
  for move in MOVES:
    if element == MOVES[move]['type'] or MOVES[move]['type'] == 'normal':
      print_move(move)
  moveset = []
  # choose three moves
  for i in range(0, 3):
    move_choice = input('Move #{}: '.format(i + 1)).lower()
    # test if move exists in movelist
    is_valid = False
    while not is_valid:
      if move_choice in MOVES and move_choice not in moveset:
        moveset.append(move_choice)
        is_valid = True
      if not is_valid:
        move_choice = input('Invalid move. Choose your move: ').lower()
  return moveset

def print_move(move):
  print(move.upper())
  print(
    "Type: {type}\tPower: {power}\tSpeed: {speed}\nInfo: {info}\n".format(
      **MOVES[move]
    )
  )

def server_first(server_elem, server_move, client_elem, client_move):
  return (
    server_elem.speed + MOVES[server_move]['speed'] > 
    client_elem.speed + MOVES[client_move]
  )

def play_as_server(client):
  if supports_ansi():
    print('\x1b[3F\x1b[J', end='') # clear initial connection text
  else:
    print()

  # CREATE CHARACTERS #
  
  server_element = pick_element()

  # given the number stat chosen, get the map for those stats
  server_stat_num = int(pick_stats()) - 1
  server_stats = STAT_OPTIONS[server_stat_num]

  # pick moveset from that elementalist's movelist of possible moves
  if server_element == 'earth':
    server_moveset = pick_moveset('earth')
  elif server_element == 'fire':
    server_moveset = pick_moveset('fire')
  elif server_element == 'water':
    server_moveset = pick_moveset('water')
  elif server_element == 'wind':
    server_moveset = pick_moveset('wind')

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
    raise SystemExit(
      'The client\'s element choice was invalid. Client may be tampering with' +
      ' the code. Exiting the program.'
    )
  # check that client chose one of the five stats options
  if client_info['stats'] not in range (1, 6):
    raise SystemExit(
      'The client\'s stats choice was invalid. Client may be tampering with ' +
      'the code. Exiting the program.'
    )
  # check that the moves are real and valid for that elementalist type
  for choice in client_info['moveset']:
    if choice not in MOVES:
      raise SystemExit(
        'The client\'s move choice was invalid. Client may be tampering with ' +
        'the code. Exiting the program.'
      )
  # finished checking client_info

  # Given the number stat chosen, get the map for those stats
  client_stat_num = int(client_info['stats']) - 1
  client_stats = STAT_OPTIONS[client_stat_num]

  client_elementalist = Elementalist(
    client_info['element'], client_stats['hp'], client_stats['attack'],
    client_stats['speed'], client_info['moveset']
  )

  print('Let the battle commence!\n\nYour moves:\n')

  # BATTLE STAGE #
  
  both_alive = True
  while both_alive:

    # choose a move
    for move in server_elementalist.moveset:
      print_move(move)
    while True: 
      server_move = input('Choose your move: ').lower()
      if server_move in server_elementalist.moveset:
        break
    # receive and validate client's move
    client_move = receive(client)
    if client_move not in client_elementalist.moveset:
      raise SystemExit(
        'The client\'s move choice was invalid. Client may be tampering with ' +
        'the code. Exiting the program.'
      )

    # evaluate speeds
    if server_first()

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

  # CREATE CHARACTER #
  
  client_element = pick_element()
  client_stats = pick_stats()
  # pick moveset from that elementalist's movelist of possible moves
  if client_element == 'earth':
    client_moveset = pick_moveset('earth')
  elif client_element == 'fire':
    client_moveset = pick_moveset('fire')
  elif client_element == 'water':
    client_moveset = pick_moveset('water')
  elif client_element == 'wind':
    client_moveset = pick_moveset('wind')

  client_info = {
    'element': client_element
    'stats': client_stats
    'moveset': client_moveset
  }
  send(server, client_info)

  # BATTLE STAGE #
  
  for move in client_elementalist.moveset:
    print_move(move)
  # push client for move until valid move entered
  while True: 
    client_move = input('Choose your move: ').lower()
    if client_move in client_elementalist.moveset:
      break
  send(server, client_move)


if __name__ == '__main__':
  if 'start' in input('Would you like to start or join? ').lower():
    with start_server_and_connect_to_client() as client:
      play_as_server(client)
  else:
    with start_client_and_connect_to_server() as server:
      play_as_client(server)
