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
<<<<<<< HEAD
print(sum)
=======
print(sum)
>>>>>>> 8a1383548bddd2f832b6813bc18492052174f35b
