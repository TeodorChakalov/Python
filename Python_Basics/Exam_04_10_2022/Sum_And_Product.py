n = int(input())

for a in range (1, 10):
    for b in range(9, a-1, -1):
        for c in range(0, 10):
            for d in range(9, c-1, -1):
                sum = a + b + c + d
                multiply = a * b * c * d

                if sum == multiply and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    exit()
                elif multiply // sum == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    exit()
print("Nothing found")