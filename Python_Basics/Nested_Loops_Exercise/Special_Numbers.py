n = int(input())

for number in range(1111, 10000):
    first_number = number // 1000
    second_number = (number // 100) % 10
    third_number = (number // 10) % 10
    fourth_number = number % 10

    if first_number != 0 and second_number != 0 and third_number != 0 and fourth_number != 0:
        if n % first_number == 0 and n % second_number == 0 and n % third_number == 0 and n % fourth_number == 0:
            print(number, end=' ')