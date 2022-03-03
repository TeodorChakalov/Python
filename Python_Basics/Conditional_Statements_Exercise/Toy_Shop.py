vacation_price = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_total_price = puzzle * 2.60
dolls_total_price = dolls * 3
bears_total_price = bears * 4.10
minions_total_price = minions * 8.20
trucks_total_price = trucks * 2

sum_count = puzzle + dolls + bears + minions + trucks
total_sum = puzzle_total_price + dolls_total_price + bears_total_price + minions_total_price + trucks_total_price

if sum_count >= 50:
    total_sum = total_sum - total_sum / 4

final_sum = total_sum - total_sum / 10

finish_price = abs(final_sum - vacation_price)

if final_sum >= vacation_price:
    print(f"Yes! {finish_price:.2f} lv left.")
else:
    print(f"Not enough money! {finish_price:.2f} lv needed.")