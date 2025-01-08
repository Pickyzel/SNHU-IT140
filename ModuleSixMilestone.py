# Tiffany McDonnell
# dictionary with rooms
rooms = {
       'Great Hall': {'South': 'Bedroom'},
       'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
       'Cellar': {'West': 'Bedroom'}
   }

# function that checks if user input is in rooms and changes the room


def get_room(current):
    print('You are currently in the {}'.format(current))
    player_input = input('What move would you like to make?').title()
    if player_input in rooms[current]:
        current = rooms[current][player_input]
    elif player_input == 'Exit':
        current = player_input
    else:
        print('Invalid Move!')
    return current


def main():
    current_room = 'Great Hall'
    live_game = True
    print('Welcome to the game')

    # a loop that operates the game

    while live_game:
        current_room = get_room(current_room)
        if current_room == 'Exit':
            live_game = False


if __name__ == "__main__":
    main()

print('You have exited the game, see you next time!')
