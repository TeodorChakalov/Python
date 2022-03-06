n = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, n+1):
    number = int(input())
    if i % 2 == 1:
        odd_sum += number
    elif i % 2 == 0:
        even_sum += number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")