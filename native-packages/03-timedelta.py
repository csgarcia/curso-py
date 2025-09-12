from datetime import timedelta, datetime

date = datetime(2023, 5, 17) + timedelta(weeks=1)  # year, month, day
date2 = datetime(2023, 6, 17)

delta = date2 - date
print(delta)
print(
    "Days:", delta.days,
    "Seconds:", delta.seconds,
    "microseconds:", delta.microseconds,
    "total_seconds:", delta.total_seconds(),
)
