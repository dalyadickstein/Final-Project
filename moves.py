MOVES = {
  'fireball': {
    'type': 'fire',
    'power': 60,
    'speed': 50,
    'info': 'Lobs a fireball that damages and may burn an opponent.',
    'effect': {
      'typ': 'burn',
      'probability': 0.7
    }
  },
  'inferno': {
    'type': 'fire',
    'power': 100,
    'speed': 10,
    'info': ('Summons a raging inferno that is so powerful, the user loses HP' +
      ' out of exhaustion.'),
    'effect': {
      'typ': 'backlash',
      'probability': 1.0,
      'severity': 15
    }
  },
  'firedance': {
    'type': 'fire',
    'power': 0,
    'speed': 60,
    'info': 'Performs a ritualistic fiery dance that boosts attack and speed.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 15,
      'spdboost': 15
    }
  },
  'pyromania': {
    'type': 'fire',
    'power': 30,
    'speed': 30,
    'info': 'A somewhat weak attack that boosts attack.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 10,
      'spdboost': 0
    }
  },
  'roast': {
    'type': 'fire',
    'power': 0,
    'speed': 40,
    'info': 'Roasts the opponent to inflict a burn.',
    'effect': {
      'typ': 'burn',
      'probability': 1.0,
    }
  },
  'fisticuffs': {
    'type': 'normal',
    'power': 40,
    'speed': 40,
    'info': 'Brawls with fists. May result in damage to oneself.',
    'effect': {
      'typ': 'backlash',
      'probability': 0.3,
      'severity': 10
    }
  }
}
