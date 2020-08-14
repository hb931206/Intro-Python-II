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


required = ['n', 's', 'e', 'w']
invalid_entry = "Please enter a valid direction"

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
print(f"You're outside")


# Write a loop that:
while True:

    # * Prints the current room name
    current_room = player.current_room


# * Prints the current description (the textwrap module might be useful here).
    # print(f"Description: {player.current_room.description} \n")

# * Waits for user input and decides what to do.

    user_input = input(
        "Choose a direction to move in ('n', 's', 'e', 'w') or press 'q' to quit ")


# If the user enters "q", quit the game.
    if user_input in required:
        player.player_move(user_input)
    elif user_input in ['q']:
        print("\nLeaving so soon?")
        break
    else:
        print(invalid_entry)
