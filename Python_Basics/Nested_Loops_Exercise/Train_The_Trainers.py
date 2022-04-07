import math

number_of_people = int(input())
name_presentation = input()

count = 0
total_sum = 0

while name_presentation != "Finish":
    sum_of_grades = 0
    for i in range(1, number_of_people+1):
        grade = float(input())
        sum_of_grades += grade
        count += 1
        total_sum += grade
    average_sum_grades = sum_of_grades / number_of_people
    print(f"{name_presentation} - {average_sum_grades:.2f}.")
    name_presentation = input()

total_sum_grades = total_sum / count
print(f"Student's final assessment is {total_sum_grades:.2f}.")