#!/usr/bin/env python

# Ghost Game

from random import randint
import os

os.system('clear')
start = """        _               _
   __ _| |__   ___  ___| |_ ___
  / _` | '_ \ / _ \/ __| __/ __|
 | (_| | | | | (_) \__ \ |_\__
  \__, |_| |_|\___/|___/\__|___/
  |___/
Gemaakt door Qi Xuan Wessel
"""

hetspook = """
       .-.
      ( " )
   /\_.' '._/|
   |         |
    \       /
     \    /`
   (__)  /
    `.__.'
"""

niethetspook = """
     .oOOOOOOo.
   oO'        'Oo
  O'  O      O  'O
 O                O
 O                O
 O  Oo,      ,oO  O
  O. 'OOOOOOOO' .O
   Yb.        .dP
     'YOOOOOOP'
"""
feeling_brave = True

print(start)
score=0

while feeling_brave:
    ghost_door = randint(1, 9)
    print('Drie deuren voor je ...\n')
    print('Een spook vlak achter je ...\n')
    print('Welke deur ga je open maken?!\n')
    door = input('1, 2,3,4,5,6,7,8 or 9?')
    door_num = int(door)
    if door_num == ghost_door:
        os.system('clear')
        print(start)
        print(hetspook)
        feeling_brave = False
    else:
        os.system('clear')
        print(start)
        os.system('sleep 1')
        print(niethetspook)
        print('Je bent door naar de volgende deur ...\n')
        score = score + 1
print('Rennen!!!!\n')
print('Game over, je score was:\n')
print(score)
