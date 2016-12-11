from moves import MOVES
from random import random, randint

def server_first(server_elem, server_move, client_elem, client_move):
  if (
    server_elem.speed + MOVES[server_move]['speed'] > 
    client_elem.speed + MOVES[client_move]['speed']
  ):
    return True
  elif (
    server_elem.speed + MOVES[server_move]['speed'] < 
    client_elem.speed + MOVES[client_move]['speed']
  ):
    return False
  else: # 50-50 chance who goes first if equal speeds
    return randint(1, 3) % 2 == 0

def is_strong(movetype, element):
  return (
    (movetype == 'fire' and element == 'wind') or
    (movetype == 'wind' and element == 'earth') or
    (movetype == 'earth' and element == 'water') or
    (movetype == 'water' and element == 'fire')
  )

def is_weak(movetype, element):
  return (
    (movetype == 'fire' and element == 'water') or
    (movetype == 'water' and element == 'earth') or 
    (movetype == 'earth' and element == 'wind') or 
    (movetype == 'wind' and element == 'fire')
  )

def attack(attacker, move, defender):
  strong = False
  weak = False
  if MOVES[move]['power'] != 0: # if it's an attack move
    damage = attacker.attack + MOVES[move]['power']
  else:
    damage = 0
  if damage != 0:
    if is_strong(MOVES[move]['type'], defender.element):
      damage *= 2
      strong = True
    if is_weak(MOVES[move]['type'], defender.element):
      damage /= 2
      weak = True
  defender.hp -= damage
  status = 'none'
  backlash = 0
  atkboost = 0
  spdboost = 0
  rando = random()
  if defender.status == 'healthy':
    if MOVES[move]['effect']['typ'] == 'burn':
      if rando < MOVES[move]['effect']['probability']:
        defender.status = 'burned'
        status = 'burned'
  if MOVES[move]['effect']['typ'] == 'backlash':
    if rando < MOVES[move]['effect']['probability']:
      backlash = MOVES[move]['effect']['severity']
      attacker.hp -= backlash
  if MOVES[move]['effect']['typ'] == 'boost':
    if rando < MOVES[move]['effect']['probability']:
      atkboost = MOVES[move]['effect']['atkboost']
      spdboost = MOVES[move]['effect']['spdboost']
      attacker.attack += atkboost
      attacker.speed += spdboost
  results = {
    'strong': strong,
    'weak': weak,
    'damage': damage,
    'status': status,
    'backlash': backlash,
    'atkboost': atkboost,
    'spdboost': spdboost
  }
  return results
