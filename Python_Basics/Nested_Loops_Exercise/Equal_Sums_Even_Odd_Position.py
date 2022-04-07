first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    num_as_string = str(number)
    even = 0
    odd = 0
    for i in range(0, len(num_as_string)):
        digit = int(num_as_string[i])
        if i % 2 == 0:
            even += digit
        else:
            odd += digit
    if odd == even:
        print(number, end=' ')