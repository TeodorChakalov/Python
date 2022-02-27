number_pages = int(input())
pages = int(input())
number_days = int(input())

total_hours = number_pages / pages
# total_hours = number_pages // pages
number_hours = total_hours / number_days
print(int(number_hours))