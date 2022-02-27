deposit_sum = float(input())
months_deposit = int(input())
annual_percent = float(input())

sum = deposit_sum + months_deposit * ((deposit_sum * annual_percent / 100) / 12)
print(sum)

# per_year = deposit_sum * (annual_percent / 100)
# per_month = per_year / 12
# sum = deposit_sum + (months_deposit * per_month)
# print(sum)