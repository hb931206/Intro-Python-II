from room import Room
from player import Player


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

wrongWay = "My gut tells me to not go over there pick another direction"

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


# Write a loop that:
while True:

    # * Prints the current room name
    current_room = player.current_room
    print(f"Location: {player.current_room.name} \n")

# * Prints the current description (the textwrap module might be useful here).
    print(f"Description: {player.current_room.description} \n")

# * Waits for user input and decides what to do.
    user_input = input(
        "Choose a direction to move in ('n', 's', 'e', 'w') or press 'q' to quit ")


# If the user enters "q", quit the game.
    if user_input == "q":
        break

# If the user enters a cardinal direction, attempt to move to the room there.

# Cardinal Directions for Outside
    if user_input == "n":
        if hasattr(current_room, "n_to"):
            player.current_room = getattr(current_room, "n_to")

        else:
            print(wrongWay)

# Cardinal Directions for Foyer
    elif user_input == "s":
        if hasattr(current_room, "s_to"):
            player.current_room = getattr(current_room, "s_to")

    elif user_input == "w":
        if hasattr(current_room, "w_to"):
            player.current_room = getattr(current_room, "w_to")

    elif user_input == "e":
        if hasattr(current_room, "e_to"):
            player.current_room = getattr(current_room, "e_to")

    else:
        print(wrongWay)
