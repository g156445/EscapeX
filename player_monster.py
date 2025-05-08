# define player and monster class
'''
1. Player class:
- Represents the player character, basic health, attack power, coordinate position and whether it holds a key.
- Starting from the starting point of the map, improve attack power through fighting and answering questions, and the ultimate goal is to escape the maze.
    default value:
        x (int): 0
        y (int): 0
        hp: 10 (full)
        attack: 0
        has_key: False

2. Monster class:
- Represents the monsters in each room of the map, randomly generates health, and attack power can be passed in according to the difficulty setting.
- Each monster will appear once in a room.
'''
import random


class Player:
    def __init__(self, name: str):
        self.name = name
        self.x = 0              #default 0
        self.y = 0              #default 0
        self.attack = 0
        self.hp = 10
        self.has_key = False

class Monster:
    def __init__(self, attack: int):
        self.hp = random.randint(10, 20)    #random set monster hp 10-20 in each map
        self.attack = attack