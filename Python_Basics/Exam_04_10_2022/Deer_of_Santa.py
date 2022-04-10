from math import floor, ceil

count_days = int(input())
food_in_kg = int(input())
food_first_deer_in_kg = float(input())
food_second_deer_in_kg = float(input())
food_third_deer_in_kg = float(input())

necessary_food_first_deer = count_days * food_first_deer_in_kg
necessary_food_second_deer = count_days * food_second_deer_in_kg
necessary_food_third_deer = count_days * food_third_deer_in_kg

total_necessary_food = necessary_food_first_deer + necessary_food_second_deer + necessary_food_third_deer

difference = abs(food_in_kg - total_necessary_food)

if food_in_kg >= total_necessary_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
