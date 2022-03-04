type_projection = input()
rows = int(input())
columns = int(input())

price = 0

if type_projection == "Premiere":
    price = 12
elif type_projection == "Normal":
    price = 7.50
elif type_projection == "Discount":
    price = 5

total_sum = price * rows * columns

print(f"{total_sum:.2f} leva")