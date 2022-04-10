count_days = int(input())

current_sum = 0
total_quantity = 0

for i in range(count_days):
    quantity_rakia = float(input())
    degree_rakia = float(input())

    total_quantity += quantity_rakia
    current_sum += quantity_rakia * degree_rakia

average_degrees = current_sum / total_quantity

print(f"Liter: {total_quantity:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")