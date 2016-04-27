import datetime

year, month, day = map(int, input().split())
days_add = int(input())


date_start = datetime.date(year, month, day)
date_end = date_start + datetime.timedelta(days=days_add)

year_end = date_end.year
month_end = date_end.month
day_end = date_end.day

# print(date_start, days_add, date_end)
print(year_end, month_end, day_end)
