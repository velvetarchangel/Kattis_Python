#Datum

import datetime

date, month = [int(x) for x in input().split()]
year = 2009
ans_day = datetime.datetime(year, month, date).weekday()
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(day_list[ans_day])
