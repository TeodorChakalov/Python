name = input()

grades = 1
count = 0
sum = 0

while grades <= 12:
    current_grade = float(input())
    if current_grade < 4.00:
        count += 1
        if count == 2:
            print(f"{name} has been excluded at {grades} grade")
            break
    else:
        sum += current_grade
        grades += 1

if count != 2:
    average = sum / 12
    print(f"{name} graduated. Average grade: {average:.2f}")

# ==================================================================================

# name = input()
#
# grades = 1
# count = 0
# sum = 0
#
# while grades <= 12 and count != 2:
#     current_grade = float(input())
#     if current_grade < 4.00:
#         count += 1
#     else:
#         sum += current_grade
#         grades += 1
#
# if count == 2:
#     print(f"{name} has been excluded at {grades} grade")
# else:
#     average = sum / 12
#     print(f"{name} graduated. Average grade: {average:.2f}")

# ==================================================================================

# name = input()
#
# average = 0.0
# counter = 0
# sum = 0.0
#
# for i in range(1, 13):
#     current_grade = float(input())
#     if current_grade >= 4.00:
#         sum += current_grade
#     else:
#         counter += 1
#     if counter == 2:
#         print(f"{name} has been excluded at {i - 1} grade")
#
# average = sum / 12
# print(f"{name} graduated. Average grade: {average:.2f}")