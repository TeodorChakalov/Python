weight_shipment = float(input())
type_service = input()
distance = int(input())

transport_per_km = 0
add_money_per_kg = 0
add_money_per_km = 0
total_add_money = 0

if type_service == "standard" or type_service == "express":
    if weight_shipment < 1:
        transport_per_km = 0.03
        add_money_per_kg = 4 * 0.03 / 5
        add_money_per_km = weight_shipment * add_money_per_kg
    elif 1 <= weight_shipment < 10:
        transport_per_km = 0.05
        add_money_per_kg = 2 * 0.05 / 5
        add_money_per_km = weight_shipment * add_money_per_kg
    elif 10 <= weight_shipment < 40:
        transport_per_km = 0.10
        add_money_per_kg = 0.10 / 20
        add_money_per_km = weight_shipment * add_money_per_kg
    elif 40 <= weight_shipment < 90:
        transport_per_km = 0.15
        add_money_per_kg = 0.15 / 50
        add_money_per_km = weight_shipment * add_money_per_kg
    elif 90 <= weight_shipment < 150:
        transport_per_km = 0.20
        add_money_per_kg = 0.20 / 100
        add_money_per_km = weight_shipment * add_money_per_kg
    if type_service == "express":
        total_add_money = distance * add_money_per_km
        final_sum = distance * transport_per_km
        total_sum = total_add_money + final_sum
        print(f"The delivery of your shipment with weight of {weight_shipment:.3f} kg. would cost {total_sum:.2f} lv.")
    else:
        final_sum = distance * transport_per_km
        print(f"The delivery of your shipment with weight of {weight_shipment:.3f} kg. would cost {final_sum:.2f} lv.")