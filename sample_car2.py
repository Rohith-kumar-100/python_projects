
def start_car(engine_off, fuel):
    if not engine_off:
        print('car is already started')
    elif fuel == 0:
        print('No fuel')
        print('car cant be turned on')
        engine_off = True

    else:
        engine_off = False
        if fuel <=  2:
            print(f'car started with low fuel: {fuel}')
            print('you can drive for only for less than 2 miles')
        else:
            print(f'car started. fuel level: {fuel}')
            print('enjoy your drive')

    return engine_off,fuel


def stop_car(engine_off, driving):
    if engine_off:
        print('car is already stopped')
    else:
        print('car is off')
        engine_off = True
        driving = False

    return engine_off, driving

def drive_car(engine_off, driving, fuel):
    if engine_off:
        driving = False
        print('turn on the car to start driving')


    elif fuel == 0:
        print('out of fuel')
        engine_off = True
        driving = False

    else:
        print('you are driving')
        fuel -= 1
        print(f'fuel left{fuel}')
        driving = True

    return engine_off, driving, fuel

def main():
    engine_off = True
    driving = False
    fuel = 5

    print('''GUIDE =
    Type start to start the car,
    Type stop to stop the car,
    Type quit to quit the game.
    Type drive to drive the game.
    ''')

    while True:
        enter = input('> ').lower()
        if enter == 'start':
            engine_off, fuel = start_car(engine_off, fuel)

        elif enter == 'stop':
            engine_off,driving = stop_car(engine_off, driving)

        elif enter == 'drive':
            engine_off,driving,fuel = drive_car(engine_off, driving, fuel)

        elif enter == 'quit':
            print('thanks for playing this game bye.')
            break

        else:
            print('unknown command. Read the guide.')


if __name__ == '__main__':
    main()
