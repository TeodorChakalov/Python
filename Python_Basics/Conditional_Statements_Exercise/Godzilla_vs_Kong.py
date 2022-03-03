budget = float(input())
statists = int(input())
price_clothing = float(input())

price_clothing_statists = statists * price_clothing
decor = budget / 10

if statists > 150:
    price_clothing_statists = price_clothing_statists - price_clothing_statists / 10

total_film_price = price_clothing_statists + decor
final_price = abs(total_film_price - budget)

if total_film_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {final_price:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {final_price:.2f} leva left.")