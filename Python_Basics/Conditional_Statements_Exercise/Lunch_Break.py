import math

serial_name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration / 8
time_for_chill = break_duration / 4

total_time_for_break = time_for_lunch + time_for_chill

remain_time = break_duration - total_time_for_break

final_time = math.ceil(abs(remain_time - episode_duration))

if remain_time >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {final_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {final_time} more minutes.")