import sys

n = int(input())

minsize = sys.maxsize
maxsize = -sys.maxsize

for i in range(1, n+1):
    number = int(input())
    if number < minsize:
        minsize = number
    if number > maxsize:
        maxsize = number

print(f"Max number: {maxsize}")
print(f"Min number: {minsize}")

