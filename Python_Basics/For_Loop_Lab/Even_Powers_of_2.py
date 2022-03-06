n = int(input())
power = 0
for i in range(0, n+1, 2):
    power = pow(2, i)
    print(power)