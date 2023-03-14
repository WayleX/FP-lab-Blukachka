"""
file contains classes important for main.py 
Classes: Person, Allie, Room, Item, Enemy
"""
class Person:
    """
    class of Person
    """
    def __init__(self, name, description):
        """
        init method
        """
        self.name = name
        self.description = description

    def describe(self):
        """
        descrive person for user
        """
        print(f'{self.name} is here!')
        print(self.description)

    def set_conversation(self, text):
        """
        sets conversation to person
        """
        self.conversation = text

    def talk(self):
        """
        makes person talk
        """
        print(f'[{self.name} says]: {self.conversation}')


class Allie(Person):
    """
    Good person in a game
    """
    def set_item(self, item):
        """
        sets item to person
        """
        self.item = item

    def get_item(self):
        """
        return item of person 
        """
        return self.item


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



class Enemy(Person):
    """
    Enemy person
    """
    def __init__(self, name, description):
        """
        init method
        """
        self.name = name
        self.description = description

    def set_weakness(self, text):
        """
        sets weakness of enemy
        """
        self.weakness = text

    def fight(self, item):
        """
        fight with player
        """
        if self.weakness == item:
            return True
        return False
