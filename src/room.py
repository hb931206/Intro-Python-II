# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
        self.items: List[Item] = []

    def compass(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to
        else:
            pass

    def __str__(self):
        return f"\nRoom: {self.name}, \nDescription: {self.description} \n"
