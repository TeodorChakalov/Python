budget = float(input())
season = input()

destination = ""
rest = ""
money = 0

if budget <= 100 and season == "summer":
    destination = "Bulgaria"
    rest = "Camp"
    money = 3 * budget / 10
elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    rest = "Hotel"
    money = 7 * budget / 10
elif 100 < budget <= 1000 and season == "summer":
    destination = "Balkans"
    rest = "Camp"
    money = 2 * budget / 5
elif 100 < budget <= 1000 and season == "winter":
    destination = "Balkans"
    rest = "Hotel"
    money = 4 * budget / 5
elif budget > 1000 and season == "summer" or season == "winter":
    destination = "Europe"
    rest = "Hotel"
    money = 9 * budget / 10

print(f"Somewhere in {destination}")
print(f"{rest} - {money:.2f}")