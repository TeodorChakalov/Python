number_pen = int(input())
number_markers = int(input())
liters = int(input())
percent_discount = int(input())

sum_without_discount = number_pen * 5.8 + number_markers * 7.2 + liters * 1.2
total_sum = sum_without_discount - percent_discount / 100 * sum_without_discount
print(total_sum)