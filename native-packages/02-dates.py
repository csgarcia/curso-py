# import time

# print(time.time())

from datetime import datetime

date = datetime(2023, 5, 17)  # year, month, day
# year, month, day, hour, minute, second
date2 = datetime(2023, 6, 17, 15, 30, 45)

now = datetime.now()

date_str = now.strptime("2023-05-17", "%Y-%m-%d")

print(date)
print(now)
print(date_str)
print(date.strftime("%Y/%m/%d"))

print(date > date2) # False

print(
  date.year,
  date.month,
  date.day,
  date.hour,
  date.minute,
  date.second,
)
