# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, current_room):

        self.current_room: Room = current_room

    def player_move(self, direction):
        if direction in ['n', 's', 'e', 'w']:
            move = self.current_room.compass(direction)
            if move is not None:
                self.current_room = move
                print(self.current_room)
            else:
                print("\n There's nothing over there...look a different direction\n")
