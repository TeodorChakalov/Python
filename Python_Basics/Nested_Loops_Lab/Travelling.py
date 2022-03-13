destination = ""

while destination != "End":
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    save_money = 0
    while save_money < budget:
        money = float(input())
        save_money += money
    print(f"Going to {destination}!")