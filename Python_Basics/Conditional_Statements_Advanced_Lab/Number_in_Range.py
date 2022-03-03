number = int(input())

is_in_interval = -100 <= number <= 100 and number != 0
if not is_in_interval:
    print("No")
else:
    print("Yes")