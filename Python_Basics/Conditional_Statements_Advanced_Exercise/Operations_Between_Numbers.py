N1 = int(input())
N2 = int(input())
operator = input()

sum = N1 + N2
subtraction = N1 - N2
multiply = N1 * N2

odd_or_even = ""

if operator == "+":
    if sum % 2 == 0:
        print(f"{N1} {operator} {N2} = {sum} - even")
    else:
        print(f"{N1} {operator} {N2} = {sum} - odd")
elif operator == "-":
    if subtraction % 2 == 0:
        print(f"{N1} {operator} {N2} = {subtraction} - even")
    else:
        print(f"{N1} {operator} {N2} = {subtraction} - odd")
elif operator == "*":
    if multiply % 2 == 0:
        print(f"{N1} {operator} {N2} = {multiply} - even")
    else:
        print(f"{N1} {operator} {N2} = {multiply} - odd")
elif operator == "/":
    if N2 != 0:
        divide = N1 / N2
        print(f"{N1} {operator} {N2} = {divide:.2f}")
    else:
        print(f"Cannot divide {N1} by zero")
elif operator == "%":
    if N2 != 0:
        remainder = N1 % N2
        print(f"{N1} {operator} {N2} = {remainder}")
    else:
        print(f"Cannot divide {N1} by zero")