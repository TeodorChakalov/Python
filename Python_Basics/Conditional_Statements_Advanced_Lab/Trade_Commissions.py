town = input()
sales = float(input())

commission = 0

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = 5 * sales / 100
    elif 500 < sales <= 1000:
        commission = 7 * sales / 100
    if 1000 < sales <= 10000:
        commission = 8 * sales / 100
    elif sales > 10000:
        commission = 12 * sales / 100
elif town == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5 * sales / 100
    elif 500 < sales <= 1000:
        commission = 7.5 * sales / 100
    if 1000 < sales <= 10000:
        commission = sales / 10
    elif sales > 10000:
        commission = 13 * sales / 100
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5 * sales / 100
    elif 500 < sales <= 1000:
        commission = 8 * sales / 100
    if 1000 < sales <= 10000:
        commission = 12 * sales / 100
    elif sales > 10000:
        commission = 14.5 * sales / 100

if commission != 0:
    print(f"{commission:.2f}")
else:
    print("error")