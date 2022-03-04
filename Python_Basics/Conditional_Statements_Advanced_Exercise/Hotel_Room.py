month = input()
count_nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < count_nights <= 14:
        studio = 47.5
    elif count_nights > 14:
        studio = 35
        apartment = 58.50
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if count_nights > 14:
        studio = studio - studio / 5
        apartment = apartment - apartment / 10
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if count_nights > 14:
        apartment = apartment - apartment / 10

total_price_apartments = apartment * count_nights
total_price_studio = studio * count_nights

print(f"Apartment: {total_price_apartments:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")