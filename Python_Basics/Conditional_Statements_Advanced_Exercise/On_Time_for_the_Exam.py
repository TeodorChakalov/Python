exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

total_exam_minutes = exam_hour * 60 + exam_minute
total_arrive_minutes = arrive_hour * 60 + arrive_minute

if total_arrive_minutes > total_exam_minutes:
    print("Late")
elif total_exam_minutes - total_arrive_minutes <= 30:
    print("On time")
elif total_exam_minutes - total_arrive_minutes > 30:
    print("Early")

result = abs(total_exam_minutes - total_arrive_minutes)

if total_exam_minutes - total_arrive_minutes > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        hours = result // 60
        minutes = result % 60
        if 0 <= minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
else:
    if result < 60:
        print(f"{result} minutes after the start")
    else:
        hours = result // 60
        minutes = result % 60
        if 0 <= minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")