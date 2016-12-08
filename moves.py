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
      'atkboost': 20,
      'spdboost': 0
    }
  },
  'roast': {
    'type': 'fire',
    'power': 0,
    'speed': 40,
    'info': 'Roasts the opponent to inflict a burn (badum-chhh).',
    'effect': {
      'typ': 'burn',
      'probability': 1.0,
    }
  },
  'fisticuffs': {
    'type': 'normal',
    'power': 70,
    'speed': 40,
    'info': 'Brawls with fists. May result in damage to oneself.',
    'effect': {
      'typ': 'backlash',
      'probability': 0.3,
      'severity': 10
    }
  },
  'jujitsu': {
    'type': 'normal',
    'power': 55,
    'speed': 75,
    'info': 'But you can do jujitsu!',
    'effect': {
      'type': 'none'
    }
  },
  'earthquake': {
    'type': 'earth',
    'power': 100,
    'speed': 10,
    'info': ('Creates an earthquake that is so powerful, the user loses HP' +
      ' out of exhaustion.'),
    'effect': {
      'typ': 'backlash',
      'probability': 1.0,
      'severity': 15
    }
  },
  'stomp': {
    'type': 'earth',
    'power': 0,
    'speed': 60,
    'info': 'Stomps and stamps on the ground to raise attack and speed.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 15,
      'spdboost': 15
    }
  },
  'stone': {
    'type': 'earth',
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
  'typhoon': {
    'type': 'water',
    'power': 100,
    'speed': 10,
    'info': ('Stirs up a massive typhoon so powerful that the user loses HP' +
      ' out of exhaustion.'),
    'effect': {
      'typ': 'backlash',
      'probability': 1.0,
      'severity': 15
    }
  },
  'synchronization': {
    'type': 'water',
    'power': 0,
    'speed': 60,
    'info': 'Boosts attack and speed utilizing synchronized swimming skills.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 15,
      'spdboost': 15
    }
  },
  'tide': {
    'type': 'water',
    'power': 0,
    'speed': 30,
    'info': 'Calls on the tide to sharply boost attack and improve speed.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 50,
      'spdboost': 15
    }
  },
  'tornado': {
    'type': 'wind',
    'power': 100,
    'speed': 10,
    'info': ('Whips up a spinning twister that is so powerful, the user loses' +
      ' HP out of exhaustion.'),
    'effect': {
      'typ': 'backlash',
      'probability': 1.0,
      'severity': 15
    }
  },
  'spiritdance': {
    'type': 'wind',
    'power': 0,
    'speed': 60,
    'info': 'Performs a spiritual dance that boosts attack and speed.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 15,
      'spdboost': 15
    }
  },
  'updraft': {
    'type': 'wind',
    'power': 30,
    'speed': 30,
    'info': 'A somewhat weak attack that boosts attack.',
    'effect': {
      'typ': 'boost',
      'probability': 1.0,
      'atkboost': 30,
      'spdboost': 0
    }
  }
}



  'dropkick': {
    'type': 'normal',
    'power': 45,
    'speed': 40,
    'info': 'Dropkicks the opponent and sometimes reduces opponent\'s speed.'
    'effect': {
      'typ': 'cripple'
      'probability': 0.5
      'severity': 15
    }
  }
