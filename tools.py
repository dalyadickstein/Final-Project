from moves import Move, Fireball, Inferno, FIRE_MOVELIST
from elementalist import Elementalist

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






def pick_moveset(movelist):
  print('Very good. It is now time to pick your moves. You may choose three:\n')
  for move in movelist:
    print_move(move)
  moveset = []
  for i in range(0, 3):
    move_choice = input('Move #{}: '.format(i + 1)).lower()
    # test if move exists in movelist
    is_valid = False
    while not is_valid:
      for move in FIRE_MOVELIST:
        if move_choice == move.name and move_choice not in moveset:
          moveset.append(move_choice)
          is_valid = True
      if not is_valid:
        move_choice = input('Invalid move. Choose your move: ').lower()
  return moveset

def print_move(move):
  print(
    '{}:\nType: {}   Power: {}   Speed: {}\nDescription: {}\n'.format(
      move.name.upper(), move.element, move.power, move.speed, move.info
    )
  )

pick_moveset(FIRE_MOVELIST)
