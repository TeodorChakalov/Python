author = input()
points_academy = float(input())
number_evaluators = int(input())

current_score = 0


for i in range(1, number_evaluators+1):
    name_evaluator = input()
    points_evaluator = float(input())

    length_name_evaluator = len(name_evaluator)
    current_score = (length_name_evaluator * points_evaluator) / 2
    points_academy += current_score

    if points_academy > 1250.5:
        print(f"Congratulations, {author} got a nominee for leading role with {points_academy:.1f}!")
        break

if points_academy <= 1250.5:
    difference = abs(1250.5 - points_academy)
    print(f"Sorry, {author} you need {difference:.1f} more!")