number_groups = int(input())

all_people = 0

people_musala = 0
people_monblan = 0
people_kilimandjaro = 0
people_K2 = 0
people_everest = 0

for i in range(1, number_groups + 1):
    number = int(input())
    all_people += number

    if number <= 5:
        people_musala += number
    elif 6 <= number <= 12:
        people_monblan += number
    elif 13 <= number <= 25:
        people_kilimandjaro += number
    elif 26 <= number <= 40:
        people_K2 += number
    elif number >= 41:
        people_everest += number

hike_musala = people_musala / all_people * 100
hike_monblan = people_monblan / all_people * 100
hike_kilimandjaro = people_kilimandjaro / all_people * 100
hike_K2 = people_K2 / all_people * 100
hike_everest = people_everest / all_people * 100

print(f"{hike_musala:.2f}%")
print(f"{hike_monblan:.2f}%")
print(f"{hike_kilimandjaro:.2f}%")
print(f"{hike_K2:.2f}%")
print(f"{hike_everest:.2f}%")