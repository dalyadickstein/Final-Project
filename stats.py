STAT_OPTIONS = [
  {'hp': 1000, 'attack': 50, 'speed': 50},
  {'hp': 1100, 'attack': 60, 'speed': 40},
  {'hp': 1500, 'attack': 30, 'speed': 30},
  {'hp': 800, 'attack': 70, 'speed': 50},
  {'hp': 900, 'attack': 50, 'speed': 75},
]


# up to you if you want this to be in this file or if you want it to be in
# game.py why game.py? 
# 
# so /usually/ things with print statements, or user interaction in general, is
# done at the highest level module (e.g. game.py) and the modules it depends on
# usually are more collections of methods / fields, and shouldn't care how they
# are ultimately "used"
# 
# so then shoudl STAT_OPTIONS be in tools.py or also in game.py?
# 
# 
# it's not a tool.  it probably belongs in its own file for organization
# purposes, which is why I created stats.py.  tools.py somehow became your goto
# for dumping random things in there haha and that's poor organization.  it
# should be for actual tools.  like generic utility functions.
# 
# how is this not utility its letting u pick ur stats. well i can rename it to 
#
# utility doesn't mean "useful" - like you should think of a tool or utility
# as a generic piece of code that just helps you do some very general logic.
# for example, you can have a utility that does some complex filtering/sorting
# logic on lists that you could see yourself using in a bunch of diff ways.
# This is not generic at all, it's a very specific part of your game.
# 
# it's about organization.  if you think STAT_OPTIONS is an important entity
# that would merit its own separate logical area of the code base, sure, give it
# a file.  
# 
# look, this logic, where you're asking the user things, is expicitly part of
# the flow of your game.  it probably belongs in game.py.  If you think that
# game.py is getting bloated, you could create another file for it 
# 
# but what about STAT_OPTIONS? sh
# o
# uld that also go into game.py or not?
# either is fine.  I think it's really up to you.  but if you're going to have
# other functions related to stat caluclations and stuff, maybe for example if
# you had a leveling or exp system or something like that, it would make sense.
# 
# I'm not saying "dalya go do a leveling / exp system" obviously it could be
# beyond the scope of your project you don't need to tell me that it's too much
# or wtvr I'm making a point about organization not about how your game works.
# 
# your modules should be organized by sections of logic they relate to.  things
# relating to stats go in stats.py. things relating to moves go into moves.py.
# but what should be in these modules is /logic/, which is entirely separate from
# asking the user stuff or printing things to the user.  in general, the I/O
# functions should be in game.py and should be entirely separate from logic -
# those functions should either only print or only get input, and then return to
# the main flow of the game.  The logic of all the steps of the game between
# going from user's input to computing output, that should start at the highest
# level in game.py and call into these other modules when it makes sense for
# that logic to live in those modules.  Does this, at a high level, make sense?
# 
# ok so what does that mean to have a function with just input and pring functions
# and no logic in them all functions have logic in them
# 
# The logic in those functions should be entirely about reading in or writing out
# data, but not about gameplay.  For example, say your game was rock paper scissors
# 
# you could have a function called getNextMove() that prompted the user "R/P/S: "
# and then checked if the input was valid and re-prompted until input was valid
# and then returned the input.  but nowhere in that function should there be
# any logic comparing the inputted move against the opponent's move to see who
# won - that's the gameplay logic and should def be a sep function. Does this
# make sense?  
# 
# nope in my main function i planned on having things being compared to opponents
# 
# in theory, your game should look like this:
# 
# 
# if main:
#   1. do setup stuff, maybe call play_as_x which effectively becomes main.
#   2. loop until game end:
#      1. send data to client for printing. (client receives)
#      2. print out on sever & client wtvr needs to be printed.
#      3. get input from server user. (client gets input from client user)
#      4. receive input from client. (client sends)
#      5. do some logic to figure out next thing to print out on each machine.
# 
# That's your game.  The input/output is totally separated from the main logic.
# In general, main shouldn't even have logic on its own, step 5 should probs
# be a separate function in game.py.  and that function will be the one that
# uses the modules like moves, elementalist, etc.
# 
# i dont understand how that would ever work with what i want to do thats useless
# u need to print stuff depending on, say, what moves they make, then print 
# more depending on their hp and their opponents hp and what damage they do, etc
# and u just said that non-main game.py functions shouldnt b doing things like 
# printing to the screen but u can't print to the screen without the logic telling
# u what ur gonna want to print to the screen.
# 
# that's what return statements are for :P
# can frikcin return some things but that still not nearly as helpful as actually 
# doing the logic right ther when u can only return one thing or map it but then u 
# hafta go through the map and access it all mapwise and its super complex

# maybe it would be better if you left the library and called?
# no i dont wanna leave the library
# I don't think I can explain this better over text.  If you want my help you
# should find a place to call.  If you think you've got it on your own, then
# keep plugging away.
# 
# well i did think i somewhat barely got something on my own but apparently the 
# organization doesnt work and changing it is bad u say evne though it would 
# technically functionally work
# 
# You don't have a working version of your code, dalya.  you don't know whether
# it will work in the way you want to, or if it does work, whether because of
# it being disorganized it will be harder for you to reason about and you'll end
# up spending many more hours on it.  
# 
#  well im gonna b spending many more hours if i rewrite it again this time again
#  with no guarantee itll b any better and will do anything other than confuse 
#  me the same way 
#  
#   which is why i said to leave the library and call me...
#   
# It does not make sense for you to on your own try to reorganize when you have
# no idea how to reorganize it better or why.  It only makes sense to reorganize
# if you have a strong sense of how to do it and what you want your code to look
# like.  Whic
# h is
#  what I want you to get to.
#  
#   ok fine ill leave library hmm
#   i guess ill try the cs building? that classroom u t
#   sur.
#   
#    meantime I'm going to get a falafel :P XD have fun how do i close teamviewer
#    or can i just shut my laptop  
# 
# 


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


# class Stats(object):

#   def __init__(self, hp, attack, speed):
#     self.hp = hp
#     self.attack = attack
#     self.speed = speed

# def pick_stats(): 
#   stat_options = [
#     stats1 = Stats(1000, 50, 50),
#     stats2 = Stats(1100, 60, 40),
#     stats3 = Stats(1500, 30, 30),
#     stats4 = Stats(800, 70, 50),
#     stats5 = Stats(900, 50, 75)
#   ]
#   n = 1
#   for stat in stat_options:
#     print("{}:\n")

# class Stats(object):
#   def __init__(self, hp, attack, speed):
#     self.hp = hp
#     self.attack = attack
#     self.speed = speed
