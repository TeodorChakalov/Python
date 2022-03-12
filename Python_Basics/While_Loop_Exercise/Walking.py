steps = 0

while steps < 10000:
    command = input()
    if command == 'Going home':
        steps_to_home = int(input())
        steps += steps_to_home
        break
    else:
        walked_steps = int(command)
        steps += walked_steps

difference = abs(steps - 10000)

if steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f"{difference} steps over the goal!")
else:
    print(f'{difference} more steps to reach goal.')


# steps = int(input())
# steps_text = str(steps)
#
# sum = 0
#
# while steps_text != "":
#     if steps_text == "Going home":
#         steps_text = input()
#         continue
#     sum += int(steps_text)
#     steps_text = input()
#
# difference = abs(sum - 10000)
#
# if sum >= 10000:
#     print("Goal reached! Good job!")
#     print(f"{difference} steps over the goal!")
# else:
#     print(f"{difference} more steps to reach goal.")