import sys

text = input()

max_number = -sys.maxsize

while text != "Stop":
    current_number = int(text)
    if current_number > max_number:
        max_number = current_number
    text = input()

print(max_number)