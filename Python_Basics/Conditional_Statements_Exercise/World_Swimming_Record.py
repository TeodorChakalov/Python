import math

records_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1_meter_swimming = float(input())

total_swim = distance_in_meters * time_in_seconds_for_1_meter_swimming
every_15_meters_increase_time = math.floor(distance_in_meters / 15) * 12.5
total_time = total_swim + every_15_meters_increase_time

record_or_not = abs(records_in_seconds - total_time)

if records_in_seconds <= total_time:
    print(f"No, he failed! He was {record_or_not:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")