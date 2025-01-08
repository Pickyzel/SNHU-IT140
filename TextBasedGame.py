# Tiffany McDonnell

# shows the commands on the command prompt based on status
def show_commands(pets):
    if 'Pet' in all_rooms[player_status[0]]:
        save_pet = input('There is a pet in the room. Would you like to save the pet?').title()

        if save_pet == 'Save':
            player_status[1] = pets + 1
            print('You have saved the {}'.format(all_rooms[player_status[0]]['Pet']))
            del all_rooms[player_status[0]]['Pet']
        else:
            print('You chose to ignore your pet.')

    if player_status[1] != 12:
        direction_input = input('What direction would you like to move?').title()
        if direction_input in all_rooms[player_status[0]]:
            player_status[0] = all_rooms[player_status[0]][direction_input]
        else:
            print('Invalid Move!')

    return

# shows how what room you are in and how many pets you have saved

def show_status():
    print('You are currently in {} and have saved {} pets'.format(player_status[0], player_status[1]))


all_rooms = {
            'Your Room': {'North': 'West Hall', 'Pet': 'Brown Dog'},
            'West Hall': {'North': 'Sisters Room', 'South': 'Your Room', 'East': 'Living Room', 'Pet': 'Gray Cat'},
            'Sisters Room': {'South': 'West Hall', 'Pet': 'Black Cat'},
            'Laundry Room': {'East': 'North Hall', 'Pet': 'Fire'},
            'Dining Room': {'North': 'Living Room', 'East': 'Kitchen', 'Pet': 'Red Bird'},
            'Living Room': {'North': 'Main Hall', 'South': 'Dining Room', 'East': 'Sun Room', 'West': 'West Hall'},
            'Computer Room': {'North': 'North Hall', 'East': 'Main Hall', 'Pet': 'Blond Hamster'},
            'North Hall': {'West': 'Laundry Room', 'South': 'Computer Room', 'East': 'Bathroom', 'Pet': 'Calico Cat'},
            'Main Hall': {'West': 'Computer Room', 'South': 'Living Room', 'Pet': 'Chocolate Hamster'},
            'Bathroom': {'West': 'North Hall', 'East': 'Parents Room', 'Pet': 'Tuxito Cat'},
            'Kitchen': {'West': 'Dining Room', 'Pet': 'Torti Cat'},
            'Sun Room': {'North': 'East Hall', 'West': 'Living Room', 'Pet': 'White Rabbit'},
            'East Hall': {'North': 'Parents Room', 'South': 'Sun Room', 'Pet': 'Silver Dog'},
            'Parents Room': {'West': 'Bathroom', 'South': 'East Hall', 'Pet': 'Yellow Bird'}
            }

player_status = ['Living Room', 0]


def main():

    live_game = True

    print('One day you were in your bedroom reading a wonderful\n'
          'adventure book when you started to smell something burning.\n'
          'You realize quickly that there is a fire that had started\n'
          'somewhere in your house, but you don’t know where.\n'
          'You think quickly that you must save all your family’s pets\n'
          'that are somewhere in the house while hoping to not encounter the flames.\n'
          'You must save 12 animals by navigating your house by typing North, South,\n'
          'East, or West and, Save to save the animal.\n'
          'If you save all the animals, you’ll be a family hero but,\n'
          'if run into the fire you’ll fall victim to the flames.')

    # loop that runs the game

    while live_game:
        if player_status[0] == 'Laundry Room':
            live_game = False
        elif player_status[1] == 12:
            live_game = False
        else:
            show_status()
            show_commands(player_status[1])


if __name__ == "__main__":
    main()

    if player_status[1] == 12:
        print('Congrats you saved all the pets and are now the family hero!')
    if player_status[0] == 'Laundry Room':
        print('You found the flames, better luck next time!')
