day = int(input())
room = input()
grade = input()

nights = day - 1

total_price_for_one_person = 0
total_price_apartment = 0
total_price_president_apartment = 0

if room == "room for one person":
    total_price_for_one_person = 18 * nights
    if grade == "positive":
        total_price_for_one_person = total_price_for_one_person + total_price_for_one_person / 4
    elif grade == "negative":
        total_price_for_one_person = total_price_for_one_person - total_price_for_one_person / 10
    print(f"{total_price_for_one_person:.2f}")
elif room == "apartment":
    total_price_apartment = 25 * nights
    if nights < 10:
        total_price_apartment = total_price_apartment - 0.5 * total_price_apartment
    elif 10 <= nights <= 15:
        total_price_apartment = total_price_apartment - 35 * total_price_apartment / 100
    elif nights > 15:
        total_price_apartment = total_price_apartment - total_price_apartment / 2
    if grade == "positive":
        total_price_apartment = total_price_apartment + total_price_apartment / 4
    elif grade == "negative":
        total_price_apartment = total_price_apartment - total_price_apartment / 10
    print(f"{total_price_apartment:.2f}")
elif room == "president apartment":
    total_price_president_apartment = 35 * nights
    if nights < 10:
        total_price_president_apartment = total_price_president_apartment - total_price_president_apartment / 10
    elif 10 <= nights <= 15:
        total_price_president_apartment = total_price_president_apartment - 15 * total_price_president_apartment / 100
    elif nights > 15:
        total_price_president_apartment = total_price_president_apartment - total_price_president_apartment / 5
    if grade == "positive":
        total_price_president_apartment = total_price_president_apartment + total_price_president_apartment / 4
    elif grade == "negative":
        total_price_president_apartment = total_price_president_apartment - total_price_president_apartment / 10
    print(f"{total_price_president_apartment:.2f}")