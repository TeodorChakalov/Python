width = int(input())
length = int(input())
count_pieces = width * length

take = input()

while take != "STOP" or count_pieces < 0:
    count_pieces -= int(take)
    if count_pieces < 0:
        break
    take = input()

if take == "STOP":
    print(f"{count_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(count_pieces)} pieces more.")