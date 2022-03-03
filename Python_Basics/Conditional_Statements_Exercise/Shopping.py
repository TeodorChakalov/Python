budget_Peter = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

total_videocards = videocards * 250
total_processors = processors * 35 * total_videocards / 100
total_ram = ram * total_videocards / 10

total_sum = total_videocards + total_processors + total_ram

if videocards > processors:
    total_sum = total_sum - 15 * total_sum / 100

remain_money = abs(budget_Peter - total_sum)

if budget_Peter >= total_sum:
    print(f"You have {remain_money:.2f} leva left!")
else:
    print(f"Not enough money! You need {remain_money:.2f} leva more!")