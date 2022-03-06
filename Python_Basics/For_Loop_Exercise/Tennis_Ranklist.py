import math

tournaments = int(input())
initially_points = int(input())

all_points = 0
win_tournaments = 0

for i in range(1, tournaments + 1):
    current_step_in_tournament = input()

    if current_step_in_tournament == "W":
        initially_points += 2000
        all_points += 2000
        win_tournaments += 1
    elif current_step_in_tournament == "F":
        initially_points += 1200
        all_points += 1200
    elif current_step_in_tournament == "SF":
        initially_points += 720
        all_points += 720

average_points_per_tournament = math.floor(all_points / tournaments)
percent_won_tournaments = win_tournaments / tournaments * 100

print(f"Final points: {initially_points}")
print(f"Average points: {average_points_per_tournament}")
print(f"{percent_won_tournaments:.2f}%")