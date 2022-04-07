film_name = input()

tickets_kid = 0
tickets_student = 0
tickets_standard = 0

total_tickets = 0

while film_name != "Finish":
    free_space = int(input())
    busy_seats = 0

    for i in range(free_space):
        type_of_ticket = input()
        if type_of_ticket == 'kid':
            tickets_kid += 1
        elif type_of_ticket == 'student':
            tickets_student += 1
        elif type_of_ticket == 'standard':
            tickets_standard += 1
        elif type_of_ticket == 'End':
            break
        total_tickets += 1
        busy_seats += 1

    percent_full_space = busy_seats / free_space * 100
    print(f"{film_name} - {percent_full_space:.2f}% full.")

    film_name = input()

percent_student_tickets = tickets_student / total_tickets * 100
percent_standard_tickets = tickets_standard / total_tickets * 100
percent_kid_tickets = tickets_kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")