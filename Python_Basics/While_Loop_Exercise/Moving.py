width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

sum = 0
command = input()

while command != "Done":
    sum += int(command)
    if sum > volume:
        print(f"No more free space! You need {sum - volume} Cubic meters more.")
        break
    command = input()

if command == "Done":
    print(f"{volume - sum} Cubic meters left.")