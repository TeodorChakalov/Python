price_day = int(input())
command = input()

count = 0
reach_income = False

while command != "closed":
    color = input()

    if command == "haircut":
        if color == "mens":
            count += 15
        elif color == "ladies":
            count += 20
        elif color == "kids":
            count += 10
    if command == "color":
        if color == "touch up":
            count += 20
        elif color == "full color":
            count += 30
    if count >= price_day:
        reach_income = True
        break

    command = input()

if count < price_day:
    difference = price_day - count
    print(f"Target not reached! You need {difference}lv. more.")
    print(f"Earned money: {count}lv.")
if reach_income:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {count}lv.")