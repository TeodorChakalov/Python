money_vacation = float(input())
available_money = float(input())

count = 0
sum = 0
count_days = 0

while available_money < money_vacation:
    spend_or_save = input()
    current_sum = float(input())

    count_days += 1

    if spend_or_save == "spend":
        available_money -= current_sum
        count += 1
        if available_money < 0:
            available_money = 0
        if count == 5:
            print("You can't save the money.")
            print(f"{count_days}")
            break
    if spend_or_save == "save":
        available_money += current_sum
        count = 0

if available_money >= money_vacation:
    print(f"You saved the money for {count_days} days.")