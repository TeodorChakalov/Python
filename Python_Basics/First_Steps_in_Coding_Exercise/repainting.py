nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

costs_nylon = nylon * 1.5
costs_paint = paint * 14.5
costs_thinner = thinner * 5

costs_paint_more = costs_paint + 0.1 * costs_paint
costs_nylon_more = costs_nylon + 3
packages = 0.4

sum_costs = costs_nylon_more + costs_paint_more + costs_thinner + packages
sum_masters = 0.3 * sum_costs * hours
total_sum = sum_costs + sum_masters
print(total_sum)