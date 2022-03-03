hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60 + minutes
time_in_minutes_plus_15 = time_in_minutes + 15

new_hour = time_in_minutes_plus_15 // 60
new_minute = time_in_minutes_plus_15 % 60

if new_hour == 24:
    new_hour = 0

if 0 <= new_minute < 10:
    print(f"{new_hour}:0{new_minute}")
else:
    print(f"{new_hour}:{new_minute}")