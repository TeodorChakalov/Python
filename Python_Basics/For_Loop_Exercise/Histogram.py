n = int(input())

sum_till_200 = 0
sum_between_200_and_400 = 0
sum_between_400_and_600 = 0
sum_between_600_and_800 = 0
sum_bigger_than_800 = 0

total_sum = 0

for i in range(0, n):
    number = int(input())
    if number < 200:
        sum_till_200 += 1
    elif 200 <= number < 400:
        sum_between_200_and_400 += 1
    elif 400 <= number < 600:
        sum_between_400_and_600 += 1
    elif 600 <= number < 800:
        sum_between_600_and_800 += 1
    elif number >= 800:
        sum_bigger_than_800 += 1

p1 = sum_till_200 / n * 100
p2 = sum_between_200_and_400 / n * 100
p3 = sum_between_400_and_600 / n * 100
p4 = sum_between_600_and_800 / n * 100
p5 = sum_bigger_than_800 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")