text = input()

balance = 0

while text != "NoMoreMoney":
    current_amount = float(text)
    if current_amount < 0:
        print("Invalid operation!")
        break
    balance += current_amount
    print(f"Increase: {current_amount:.2f}")
    text = input()

print(f"Total: {balance:.2f}")

