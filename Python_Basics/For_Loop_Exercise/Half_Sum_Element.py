import sys
max_number = -sys.maxsize

n = int(input())

sum = 0

for i in range(0, n):
    number = int(input())
    if number > max_number:
        max_number = number
    sum += number

sum_numbers_without_max_number = sum - max_number

if sum_numbers_without_max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(sum_numbers_without_max_number - max_number)
    print("No")
    print(f"Diff = {difference}")