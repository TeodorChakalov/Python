flowers = input()
count_flowers = int(input())
budget = int(input())

total_sum = 0

if flowers == "Roses":
    total_sum = count_flowers * 5
    if count_flowers > 80:
        total_sum = total_sum - total_sum / 10
elif flowers == "Dahlias":
    total_sum = count_flowers * 3.80
    if count_flowers > 90:
        total_sum = total_sum - 15 * total_sum / 100
elif flowers == "Tulips":
    total_sum = count_flowers * 2.80
    if count_flowers > 80:
        total_sum = total_sum - 15 * total_sum / 100
elif flowers == "Narcissus":
    total_sum = count_flowers * 3
    if count_flowers < 120:
        total_sum = total_sum + 15 * total_sum / 100
elif flowers == "Gladiolus":
    total_sum = count_flowers * 2.50
    if count_flowers < 80:
        total_sum = total_sum + total_sum / 5

remain_money = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} and {remain_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {remain_money:.2f} leva more.")