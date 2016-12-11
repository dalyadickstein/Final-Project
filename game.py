import platform
import os
import sys
import time

from random import randint, random
from stats import STAT_OPTIONS
from moves import MOVES
from elementalist import Elementalist
from fight import server_first, attack, is_strong, is_weak
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
  print('Next, choose which set of stats you want.\n')
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
      print('\n')
      return stats

def pick_element():
  print('\nElementalist! Choose your element!\n')
  time.sleep(1)
  print('Will your spirit burn like Fire?')
  time.sleep(1)
  print('Or be both tranquil and tempestuous as Water?')
  time.sleep(1)
  print('Are you as invisible and powerful as Wind?')
  time.sleep(1)
  print('Or as unyielding as the Earth itself?\n')
  time.sleep(1)
  element = input('Your element: ').lower()
  while True:
    if (
      element == 'fire' or element == 'water' or 
      element == 'wind' or element == 'earth'
    ):
      print('\n')
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
      if (
        move_choice in MOVES and 
        move_choice not in moveset and
        (MOVES[move_choice]['type'] == 'normal' or 
        MOVES[move_choice]['type'] == element)
      ):
        moveset.append(move_choice)
        is_valid = True
      if not is_valid:
        move_choice = input('Invalid move. Choose your move: ').lower()
  print('\n')
  return moveset

def print_move(move):
  print(move.upper())
  print(
    'Type: {type}\tPower: {power}\tSpeed: {speed}\nInfo: {info}\n'.format(
      **MOVES[move]
    )
  )

# what prints to your screen when you make an attack
def print_atk_results(results):
  if results['strong']:
    print('It\'s super effective against your opponent!')
  if results['weak']:
    print(
      'Unfortunately, your move\'s type is weak against this particular ' +
      'opponent.'
    )
  if results['damage'] != 0:
    print('You dealt {} damage!'.format(results['damage']))
  if results['status'] == 'burned':
    print('Your opponent was burned!')
  if results['backlash'] != 0:
    print(
      'You were hurt in the fracas and lost {} HP.'.format(results['backlash'])
    )
  if results['atkboost'] != 0:
    print('Your attack was boosted by {} points!'.format(results['atkboost']))
  if results['spdboost'] != 0:
    print('Your speed was boosted by {} points!'.format(results['spdboost']))
  wait()

# what prints to your screen when you are attacked by the opponent
def print_def_results(results):
  if results['strong']:
    print('The opponent launches a devastating attack!')
  if results['weak']:
    print(
      'You easily shake off your opponent\'s ill-planned, ineffective attack.'
    )
  if results['damage'] != 0:
    print('You lose {} HP!'.format(results['damage']))
  if results['status'] == 'burned':
    print('Ssssszzz! Agh! You were burned!')
  if results['backlash'] != 0:
    print(
      'You\'re pleased to see that your opponent is at least injured in the ' +
      'tussle, sustaining {} damage.'.format(results['backlash'])
    )
  if results['atkboost'] != 0:
    print(
      'Your opponent\'s attack is boosted by {} points!'.format(
        results['atkboost']
      )
    )
  if results['spdboost'] != 0:
    print(
      'Your opponent\'s speed is boosted by {} points!'.format(
        results['spdboost']
      )
    )
  wait()

def wait():
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)

def knocked_out(your_hp, opponent_hp):
  if your_hp > 0 and opponent_hp <= 0:
    print(
      'You smite your opponent upon the slopes of the great mountain.\n' +
      'You have won. Well fought, elementalist.\n\n'
    )
    return True
  elif your_hp <= 0 and opponent_hp > 0:
    print(
      'You fall to your knees, unable to hold yourself up any longer as your ' +
      'head swims and your vision darkens, and you fall slowly into the ' +
      'abyss.\nYou have fallen.\n\n'
    )
    return True
  elif your_hp <= 0 and opponent_hp <= 0:
    print(
      'In one final, mighty clash, you both throw yourselves at each other ' +
      'with all of your remaining strength.\nYou are evenly matched until ' +
      'the end.\nYou fall there, side by side, equals in both life and death.' +
      '\n\n'
    )
    return True
  else:
    return False

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
  if int(client_info['stats']) not in range (1, 6):
    raise SystemExit(
      'The client\'s stats choice was invalid. Client may be tampering with ' +
      'the code. Exiting the program.'
    )
  # check that the moveset is valid
  for choice in client_info['moveset']:
    # check that choice is a valid type for that elementalist
    valid_choice = False
    if client_info['element'] == 'earth':
      if MOVES[choice]['type'] == 'earth':
        valid_choice = True
    elif client_info['element'] == 'fire':
      if MOVES[choice]['type'] == 'fire':
        valid_choice = True
    elif client_info['element'] == 'water':
      if MOVES[choice]['type'] == 'water':
        valid_choice = True
    elif client_info['element'] == 'wind':
      if MOVES[choice]['type'] == 'wind':
        valid_choice = True
    # normal type moves are valid for all elementalists
    if MOVES[choice]['type'] == 'normal':
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

  # BATTLE STAGE #
  
  wait()
  print('Let the battle commence!')
  wait()
  
  while True:

    # choose a move
    print('Your moves:\n')
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
    wait() # call wait before printing results for nicer user experience
    # evaluate speeds
    if server_first(
      server_elementalist, server_move, client_elementalist, client_move
    ):
      server_second = False
      # if server's first, server attacks client
      server_atk_results = attack(
        server_elementalist, server_move, client_elementalist
      )
      # let client know which results these are
      server_atk_results['attacker'] = 'server'
      # tell client the hp of each after the attack
      server_atk_results['server_hp'] = server_elementalist.hp
      server_atk_results['client_hp'] = client_elementalist.hp
      send(client, server_atk_results)
      print_atk_results(server_atk_results)
      if knocked_out(server_elementalist.hp, client_elementalist.hp):
        break
    else:
      server_second = True
    # client attacks server
    client_atk_results = attack(
      client_elementalist, client_move, server_elementalist
    )
    client_atk_results['attacker'] = 'client'
    client_atk_results['server_hp'] = server_elementalist.hp
    client_atk_results['client_hp'] = client_elementalist.hp
    send(client, client_atk_results)
    print_def_results(client_atk_results)
    if knocked_out(server_elementalist.hp, client_elementalist.hp):
      break
    # if server hadn't been first, server attacks client
    if server_second:
      server_atk_results = attack(
        server_elementalist, server_move, client_elementalist
      )
      server_atk_results['attacker'] = 'server'
      server_atk_results['server_hp'] = server_elementalist.hp
      server_atk_results['client_hp'] = client_elementalist.hp
      send(client, server_atk_results)
      print_atk_results(server_atk_results)
      if knocked_out(server_elementalist.hp, client_elementalist.hp):
        break

    # status conditions
    if server_elementalist.status == 'burned':
      print('You lose 25 HP from your burn.')
      wait()
      server_elementalist.hp -= 25
    if client_elementalist.status == 'burned':
      print('Your opponent loses 25 HP from burns.')
      wait()
      client_elementalist.hp -= 25

    # send status condition info to client
    status_info = {
      'server_status': server_elementalist.status,
      'client_status': client_elementalist.status,
      'server_hp': server_elementalist.hp,
      'client_hp': client_elementalist.hp
    }
    send(client, status_info)

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
    'element': client_element,
    'stats': client_stats,
    'moveset': client_moveset
  }
  send(server, client_info)

  # BATTLE STAGE #
  
  wait()
  print('Let the battle commence!')
  wait()
  
  while True:

    print('Your moves:\n')
    for move in client_moveset:
      print_move(move)
    # push client for move until valid move entered
    while True: 
      client_move = input('Choose your move: ').lower()
      if client_move in client_moveset:
        break
    send(server, client_move)
    wait() # wait before printing results for better user experience

    # faster player's attack results
    results = receive(server)
    if results['attacker'] == 'server':
      print_def_results(results)
    else:
      print_atk_results(results)

    # check if game over
    if knocked_out(results['client_hp'], results['server_hp']):
      break

    # slower player's attack results
    results = receive(server)
    if results['attacker'] == 'server':
      print_def_results(results)
    else:
      print_atk_results(results)

    # check if game over
    if knocked_out(results['client_hp'], results['server_hp']):
      break

    # receive status info
    status_info = receive(server)
    if status_info['server_status'] == 'burned':
      print('Your opponent loses 25 HP from burns.')
      wait()
    if status_info['client_status'] == 'burned':
      print('You lose 25 HP from your burn.')
      wait()
    if knocked_out(status_info['client_hp'], status_info['server_hp']):
      break

if __name__ == '__main__':
  if 'start' in input('Would you like to start or join? ').lower():
    with start_server_and_connect_to_client() as client:
      play_as_server(client)
  else:
    with start_client_and_connect_to_server() as server:
      play_as_client(server)
