age = int(input())
price_laundry = float(input())
price_toy = int(input())

total_sum = 0
count = 1
count_toys = 0

for i in range(1, age+1):
    if i % 2 == 0:
        total_sum += 10 * count
        count += 1
    else:
        count_toys += 1

total_price_toys = price_toy * count_toys
total_save_money = total_sum + total_price_toys - count + 1

difference = abs(total_save_money - price_laundry)

if total_save_money >= price_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")


# age = int(input())
# price_laundry = float(input())
# price_toy = int(input())
#
# count = 10
# all_saving = 0
# count_toys = 0
#
# for i in range(1, age+1):
#     if i % 2 == 0:
#         all_saving += count
#         count += 10
#         all_saving -= 1
#     else:
#         count_toys += 1
#
# total_price_toys = price_toy * count_toys
# total_save_money = all_saving + total_price_toys
#
# difference = abs(total_save_money - price_laundry)
#
# if total_save_money >= price_laundry:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {difference:.2f}")