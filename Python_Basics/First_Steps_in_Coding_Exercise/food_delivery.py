chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

total_chicken_menu = chicken_menu * 10.35
total_fish_menu = fish_menu * 12.4
total_vegan_menu = vegan_menu * 8.15

sum = total_chicken_menu + total_fish_menu + total_vegan_menu
desert = 0.2 * sum
total_sum = sum + desert + 2.5
print(total_sum)