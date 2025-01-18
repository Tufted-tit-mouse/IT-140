def startMenu():
    print('Welcome to the mall raid!')
    print('Collect all 6 items or get killed by Killa!')
    print('Move command: go South, go North, go West, or go East')
    print('Add to inventory: get \'item name\'')
    print()


def stats(currentRoom, currentList, rooms):
    print('You are at {}'.format(currentRoom))
    print('Inventory {}'.format(currentList))
    if 'item' in rooms[currentRoom]:
        print('{} is in {}'.format(rooms[currentRoom]['item'], currentRoom))
    print('_____________________________________')


def killa():
    print('Raid ended!')
    print('You have been killed in action!')
    print('   +----------+')
    print('  |  || || ||  |')
    print(' |   || || ||   |')
    print('|    || || ||    |')
    print('|    --------    |')
    print('|    || || ||    |')
    print('|    || || ||    |')
    print('|    || || ||    |')
    print(' |   || || ||   |')
    print('  +------------+')


def victory():
    print('Raid ended!')
    print('You survived!!!!!')


def main():
    rooms = {
        'Front Door': {'North': 'Goshan', 'East': 'Brutal', 'West': 'Mantis'},
        'Mantis': {'North': 'German', 'East': 'Front Door', 'West': 'Emercom', 'item': 'Ifak'},
        'Emercom': {'East': 'Mantis', 'item': 'Propital'},
        'German': {'South': 'Mantis', 'East': 'Goshan', 'item': 'Backpack'},
        'Goshan': {'South': 'Front Door', 'West': 'German', 'East': 'Kiba', 'item': 'Toshonka'},
        'Kiba': {'South': 'Brutal', 'East': 'Generic', 'West': 'Goshan', 'item': 'M4'},
        'Generic': {'West': 'Kiba', 'item': 'Ammo'},
        'Brutal': {'West': 'Front Door', 'item': 'Killa'}
    }
    currentRoom = 'Front Door'
    currentList = []


    startMenu()
    while True:
        if len(currentList) == 6:
            victory()
            break
        elif currentRoom == 'Brutal':
            killa()
            break
        else:
            stats(currentRoom, currentList, rooms)
            direction = input('Enter next direction: ').split(' ')
            print()
            if (direction[0] == 'go') and (direction[1] in rooms[currentRoom]):
                currentRoom = rooms[currentRoom][direction[1]]
            elif direction[0] == 'get':
                if 'item' in rooms[currentRoom]:
                    currentList.append(direction[1])
                    print('{} added to inventory'.format(direction[1]))
                    del rooms[currentRoom]['item']
                else:
                    print('Can\'t get {}'.format(direction[1]))
                    print()
            else:
                print()
                print('Invalid option:')
                print()


main()
