"""
File contains important classes for main.py
Classes: Room, Item, Enemy
"""
class Room:
    """
    Room class
    contains all interaction with room in a game
    """
    def __init__(self, name):
        """
        init method
        """
        self.name = name
        self.character = None
        self.room_item = None
        self.connections = []

    def set_description(self, text):
        """
        set description for room
        """
        self.description = text

    def set_character(self, chrc):
        """
        set character in room 
        """
        self.character = chrc

    def set_item(self, item):
        """
        set item to room 
        """
        self.room_item = item

    def link_room(self, room, direct):
        """
        link room with other room by direction - west,east etc
        """
        self.connections.append([room, direct])

    def get_details(self):
        """
        details of room for user
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for elem in self.connections:
            print(f'The {elem[0].name} is {elem[1]}')

    def get_character(self):
        """
        get current room character
        """
        return self.character

    def get_item(self):
        """
        get current room item
        """
        return self.room_item

    def move(self, to):
        """
        move to neighbour room
        """
        for elem in self.connections:
            if elem[1] == to:
                return elem[0]


class Item:
    """
    Class of item placed in a room
    """
    def __init__(self, name):
        """
        init method
        """
        self.name = name

    def get_name(self):
        """
        get name of item
        """
        return self.name

    def set_description(self, text):
        """
        set description for item
        """
        self.description = text

    def describe(self):
        """
        descrive item for player
        """
        print(f'The [{self.name}] is here - {self.description}')


class Enemy:
    """
    Class of enemy located in a room
    """
    kills = 0

    def __init__(self, name, description):
        """
        init method
        """
        self.name = name
        self.description = description

    def describe(self):
        """
        describe enemy for user
        """
        print(f'{self.name} is here!')
        print(self.description)

    def set_conversation(self, text):
        """
        set conversation to enemy
        """
        self.conversation = text

    def set_weakness(self, text):
        """
        set weakness to enemy
        """
        self.weakness = text

    def fight(self, item):
        """
        simulation of fight
        """
        if self.weakness == item:
            return True
        return False

    def get_defeated(self):
        """
        count of kills
        """
        Enemy.kills += 1
        return Enemy.kills

    def talk(self):
        """
        talking with enemy
        """
        print(f'[{self.name} says]: {self.conversation}')
