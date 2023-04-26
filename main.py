# Daulton Truett

def show_intro():
    print('Treasure Island adventure')
    print()
    print('You have set out on an adventure to find treasure that has been rumored to be hidden across a small set of '
          'islands. Each island will either have one treasure hidden on it or nothing at all. The only problem is your '
          'not the only one looking for treasure out on the open sea! Pirates have been known to sail between these '
          'islands searching for the elusive treasures. You must collect all 9 treasures without being caught by the '
          'pirates in order to win. Have Fun and travel smart!')
    print()
    print('Helpful tips: '
          'To travel between islands, simply type a direction when asked. "north, south, east, or west" '
          'To pick up items as you see them, type "yes" , these treasures will be added to your '
          'inventory. If you have all 9 treasures before getting caught by the pirates you win!')
    print()
    print()


def get_treasure_input_from_player(inventory, islands, player_location):
    if islands[player_location]['treasure']:
        print()
        print('You see a {}'.format(islands[player_location]['treasure']))
        get_item = input('Pick up item? ')
        print()
        if get_item == 'yes':
            print('...Adding {}'.format(
                islands[player_location]['treasure']), 'to you inventory...')
            print('You picked up a {}'.format(
                islands[player_location]['treasure']), 'and added it to your inventory')
            inventory.append(islands[player_location]['treasure'])
            islands[player_location]['treasure'] = None


def get_movement_input_from_player(islands, player_location):
    player_move_input = input(
        'Which direction would you like to go? ').lower()
    new_player_location = player_location
    if player_move_input in islands[player_location]:
        new_player_location = islands[player_location][player_move_input]
    else:
        print('move not valid, pick another direction')
        get_movement_input_from_player(islands, player_location)
    return new_player_location


def available_moves(player_location):
    if player_location == 'central island':
        print('You can move: north, south, east, or west ')
    elif player_location == 'south island':
        print('You can move: north')
    elif player_location == 'north island':
        print('You can move: south or east')
    elif player_location == 'far away island':
        print('You can move: south or west')
    elif player_location == 'the banks':
        print('You can move: north or south')
    elif player_location == 'east island':
        print('You can move: north, south, or west')
    elif player_location == 'the bottoms':
        print('You can move: north or west')
    elif player_location == 'west island':
        print('You can move: east or south')
    elif player_location == 'no pass island':
        print('You can move: north or south')
    else:
        pass


def main():
    player_location = 'central island'  # starting location
    inventory = []  # starting inventory
    islands = {
        'central island': {
            'north': 'north island',
            'south': 'south island',
            'east': 'east island',
            'west': 'west island',
            'treasure': None
        },
        'south island': {
            'north': 'central island',
            'treasure': 'copper bar'
        },
        'north island': {
            'south': 'central island',
            'east': 'far away island',
            'treasure': 'jewel'
        },
        'far away island': {
            'south': 'the banks',
            'west': 'north island',
            'treasure': 'gold coin'
        },
        'the banks': {
            'north': 'far away island',
            'south': 'east island',
            'treasure': 'pack of smokes'
        },
        'east island': {
            'north': 'the banks',
            'south': 'the bottoms',
            'west': 'central island',
            'treasure': 'silver coin'
        },
        'the bottoms': {
            'north': 'east island',
            'west': 'lost island',
            'treasure': 'platinum bar'
        },
        'west island': {
            'east': 'central island',
            'south': 'no pass island',
            'treasure': 'silver bar'
        },
        'no pass island': {
            'north': 'west island',
            'south': 'lost island',
            'treasure': 'bottle of rum'
        },
        'lost island': {
            'villain': 'pirates',
            'treasure': None
        }
    }
    show_intro()
    while player_location != 'lost island' and len(inventory) < 8:
        print()
        print('-----------------------------------------------------')
        print('You are on {}'.format(player_location))

        available_moves(player_location)

        print('Inventory :', inventory)
        print('-----------------------------------------------------')
        print()
        player_location = get_movement_input_from_player(
            islands, player_location)
        get_treasure_input_from_player(inventory, islands, player_location)
        if player_location == 'lost island':
            print("You landed on 'lost island' and the pirates caught you! ")
            print("Try again..")
        elif len(inventory) == 8:
            print('You win!!')
        else:
            pass


main()
