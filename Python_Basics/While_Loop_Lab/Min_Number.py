import sys

text = input()

min_number = sys.maxsize

while text != "Stop":
    current_number = int(text)
    if current_number < min_number:
        min_number = current_number
    text = input()

print(min_number)