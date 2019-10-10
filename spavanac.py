hour, minute = [int(x) for x in input().split()]
alarm_hour = 0
alarm_minute = 0

if (hour == 0 and minute < 45):
    alarm_hour = 23
    alarm_minute = minute + 15
elif (hour == 0 and minute > 45):
    alarm_hour = 0
    alarm_minute = minute - 45
elif (hour != 0 and minute < 45):
    alarm_hour = hour - 1
    alarm_minute = minute +15
elif (hour != 0 and minute > 45):
    alarm_hour = hour
    alarm_minute = minute - 45

print(str(alarm_hour) + " " + str(alarm_minute))
