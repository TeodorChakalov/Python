count_people = int(input())
count_nights = int(input())
count_cards_transport = int(input())
count_tickets_museum = int(input())

nights = count_nights * 20
cards_transport = count_cards_transport * 1.60
tickets_museum = count_tickets_museum * 6

total_sum_per_person = nights + cards_transport + tickets_museum
total_sum = total_sum_per_person * count_people

total_sum_after_expenses = total_sum + total_sum / 4

print(f"{total_sum_after_expenses:.2f}")
