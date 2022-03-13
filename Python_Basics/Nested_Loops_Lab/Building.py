floors = int(input())
rooms = int(input())

for number_of_floor in range(floors, 0, -1):
    for number_of_apartment in range(0, rooms):
        if number_of_floor == floors:
            print(f"L{number_of_floor}{number_of_apartment} ", end='')
        elif number_of_floor % 2 == 1:
            print(f"A{number_of_floor}{number_of_apartment} ", end='')
        elif number_of_floor % 2 == 0:
            print(f"O{number_of_floor}{number_of_apartment} ", end='')
    print()