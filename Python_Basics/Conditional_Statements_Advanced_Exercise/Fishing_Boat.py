budget = int(input())
season = input()
count_fishers = int(input())

price_spring = 3000
price_summer_autumn = 4200
price_winter = 2600

total_price = 0

if season == "Spring":
    if count_fishers <= 6:
        total_price = 2700
    elif 7 <= count_fishers <= 11:
        total_price = price_spring - 15 * price_spring / 100
    elif count_fishers >= 12:
        total_price = price_spring - price_spring / 4
elif season == "Summer":
    if count_fishers <= 6:
        total_price = 3780
    elif 7 <= count_fishers <= 11:
        total_price = price_summer_autumn - 15 * price_summer_autumn / 100
    elif count_fishers >= 12:
        total_price = price_summer_autumn - price_summer_autumn / 4
elif season == "Autumn":
    if count_fishers <= 6:
        total_price = 3780
    elif 7 <= count_fishers <= 11:
        total_price = price_summer_autumn - 15 * price_summer_autumn / 100
    elif count_fishers >= 12:
        total_price = price_summer_autumn - price_summer_autumn / 4
elif season == "Winter":
    if count_fishers <= 6:
        total_price = 2340
    elif 7 <= count_fishers <= 11:
        total_price = price_winter - 15 * price_winter / 100
    elif count_fishers >= 12:
        total_price = price_winter - price_winter / 4

if season == "Spring" or season == "Summer" or season == "Winter":
    if count_fishers % 2 == 0:
        total_price = total_price - total_price / 20

remain_money = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {remain_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {remain_money:.2f} leva.")