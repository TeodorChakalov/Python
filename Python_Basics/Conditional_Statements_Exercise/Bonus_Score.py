number = int(input())

if number <= 100:
    bonus = 5
elif 100 < number <= 1000:
    bonus = number / 5
elif number > 1000:
    bonus = number / 10

if number % 2 == 0:
    bonus += 1
if number % 10 == 5:
    bonus += 2

sum = number + bonus

print(bonus)
print(sum)

role = "Administrator"
if role != "Administrator":
    print("No permission")
else:
    print("Welcome")

