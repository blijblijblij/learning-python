#!/usr/bin/env python

# Ghost Game

from random import randint
print('Ghost Game')
feeling_brave = True
score=0

while feeling_brave:
    ghost_door = randint(1, 3)
    print('Drie deuren voor je ...')
    print('Een spook vlak achter je ...')
    print('Welke deur ga je open maken?!')
    door = input('1, 2, or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('HET SPOOK!!!!!')
        feeling_brave = False
    else:
        print('Geen spook!')
        print('Je bent door naar de volgende deur ...')
        score = score + 1
print('Rennen!!!!')
print('Game over, je score was ', score)
