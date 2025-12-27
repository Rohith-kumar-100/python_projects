
Engine_off = True
driving = False
fuel = 5
print('''GUIDE =
Type start to start the car,
Type stop to stop the car,
Type quit to quit the game.
Type drive to drive the game.
''')
while True:
    enter = input('> ')

    if enter == 'start':
        if not Engine_off:
            print('car is already started')
        elif fuel == 0:
            print('No fuel')
            print('car cant be turned on')
            Engine_off = True

        else:
            Engine_off = False
            if fuel <=  2:
                print(f'car started with low fuel: {fuel}')
                print('you can drive for only for less than 2 miles')
            else:
                print(f'car started. fuel level: {fuel}')
                print('enjoy your drive')


    elif enter == 'stop':
        if Engine_off:
            print('car is already stopped')
        else:
            print('car is off')
            Engine_off = True
            driving = False

    elif enter == 'quit':
        print('Thank you for playing')
        break

    elif enter == 'drive':
        if Engine_off:
            driving = False
            print('turn on the car to start driving')


        elif fuel == 0:
            print('out of fuel')
            Engine_off = True
            driving = False

        else:
            print('you are driving')
            fuel -= 1
            print(f'fuel left{fuel}')
            driving = True

    else:
        print('invalid input please try again')


