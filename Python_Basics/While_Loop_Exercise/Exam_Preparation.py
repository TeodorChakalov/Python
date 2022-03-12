count_grades = int(input())

sum = 0
sum_grades = 0
count = 0
finish_task = ""
task_name = input()

while task_name != "Enough":
    grade = int(input())

    sum += 1
    sum_grades += grade

    if grade <= 4:
        count += 1
        if count == count_grades:
            break
    finish_task = task_name
    task_name = input()

if task_name == "Enough":
    average = sum_grades / sum
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {sum}")
    print(f"Last problem: {finish_task}")
else:
    print(f"You need a break, {count_grades} poor grades.")