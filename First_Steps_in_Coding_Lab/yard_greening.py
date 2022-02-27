square_meters = float(input())
price_without_discount = square_meters * 7.61
final_price = price_without_discount - 0.18 * price_without_discount
discount = price_without_discount - final_price

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount:.2f} lv.")