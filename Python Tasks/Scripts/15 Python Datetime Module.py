# ============================================================
# DATETIME MODULE — COMPLETE PYTHON SCRIPT
# ============================================================

from datetime import datetime, date, time, timedelta


# ============================================================
# 1. CURRENT DATE AND TIME
# ============================================================

now = datetime.now()

print("Current datetime:")
print(now)

print()


# ============================================================
# 2. CURRENT DATE
# ============================================================

today = date.today()

print("Today's date:")
print(today)

print()


# ============================================================
# 3. CURRENT TIME
# ============================================================

current_time = datetime.now().time()

print("Current time:")
print(current_time)

print()


# ============================================================
# 4. GET INDIVIDUAL PARTS
# ============================================================

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

print()


# ============================================================
# 5. CREATE A SPECIFIC DATE
# ============================================================

birthday = date(2001, 11, 4)

print("Birthday:")
print(birthday)

print()


# ============================================================
# 6. CREATE A SPECIFIC DATETIME
# ============================================================

event_time = datetime(2026, 9, 6, 14, 30, 0)

print("Event datetime:")
print(event_time)

print()


# ============================================================
# 7. CREATE A SPECIFIC TIME
# ============================================================

meeting_time = time(14, 30, 0)

print("Meeting time:")
print(meeting_time)

print()


# ============================================================
# 8. FORMAT DATETIME → STRING
# ============================================================

# strftime() = string format time

formatted = now.strftime("%Y-%m-%d")

print("Formatted date:")
print(formatted)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted datetime:")
print(formatted)

print()


# ============================================================
# COMMON FORMAT CODES
# ============================================================

print("Year:", now.strftime("%Y"))
print("Month:", now.strftime("%m"))
print("Day:", now.strftime("%d"))

print("Hour:", now.strftime("%H"))
print("Minute:", now.strftime("%M"))
print("Second:", now.strftime("%S"))

print("Day name:", now.strftime("%A"))
print("Month name:", now.strftime("%B"))

print()


# ============================================================
# 9. STRING → DATETIME
# ============================================================

# strptime() = string parse time

date_string = "2026-09-06"

converted_date = datetime.strptime(
    date_string,
    "%Y-%m-%d"
)

print("String converted to datetime:")
print(converted_date)

print()


# ============================================================
# 10. STRING → DATETIME WITH TIME
# ============================================================

date_string = "2026-09-06 15:30:45"

converted_datetime = datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S"
)

print("Converted datetime:")
print(converted_datetime)

print()


# ============================================================
# 11. DATE ARITHMETIC
# ============================================================

tomorrow = today + timedelta(days=1)

print("Today:")
print(today)

print("Tomorrow:")
print(tomorrow)

print()


# ============================================================
# 12. ADD DAYS
# ============================================================

next_week = today + timedelta(days=7)

print("Next week:")
print(next_week)

print()


# ============================================================
# 13. SUBTRACT DAYS
# ============================================================

yesterday = today - timedelta(days=1)

print("Yesterday:")
print(yesterday)

print()


# ============================================================
# 14. ADD HOURS
# ============================================================

future_time = now + timedelta(hours=5)

print("5 hours from now:")
print(future_time)

print()


# ============================================================
# 15. ADD MINUTES
# ============================================================

future_time = now + timedelta(minutes=30)

print("30 minutes from now:")
print(future_time)

print()


# ============================================================
# 16. DIFFERENCE BETWEEN TWO DATES
# ============================================================

start_date = date(2026, 9, 1)
end_date = date(2026, 9, 6)

difference = end_date - start_date

print("Date difference:")
print(difference)

print("Number of days:")
print(difference.days)

print()


# ============================================================
# 17. DIFFERENCE BETWEEN TWO DATETIMES
# ============================================================

start = datetime(2026, 9, 6, 10, 0, 0)
end = datetime(2026, 9, 6, 15, 30, 0)

duration = end - start

print("Duration:")
print(duration)

print("Total seconds:")
print(duration.total_seconds())

print()


# ============================================================
# 18. COMPARE DATES
# ============================================================

date1 = date(2026, 9, 1)
date2 = date(2026, 9, 6)

if date2 > date1:
    print("date2 is after date1")

print()


# ============================================================
# 19. CHECK IF DATE IS IN THE PAST
# ============================================================

deadline = date(2026, 9, 1)

if deadline < today:
    print("Deadline has passed")
else:
    print("Deadline has not passed")

print()


# ============================================================
# 20. CHECK IF DATE IS IN THE FUTURE
# ============================================================

future_date = date(2026, 12, 31)

if future_date > today:
    print("Future date")

print()


# ============================================================
# 21. DAY OF WEEK
# ============================================================

# Monday = 0
# Tuesday = 1
# Wednesday = 2
# ...
# Sunday = 6

print("Day number:", today.weekday())
print("Day name:", today.strftime("%A"))

print()


# ============================================================
# 22. ISO FORMAT
# ============================================================

print("ISO format:")
print(now.isoformat())

print()


# ============================================================
# 23. DATA ENGINEERING EXAMPLE
# ============================================================

# Imagine this timestamp came from a log/event.

raw_timestamp = "2026-09-06 12:45:30"

event_time = datetime.strptime(
    raw_timestamp,
    "%Y-%m-%d %H:%M:%S"
)

print("Original event:")
print(event_time)

print("Event date:")
print(event_time.date())

print("Event hour:")
print(event_time.hour)

print("Event year:")
print(event_time.year)

print("Event month:")
print(event_time.month)

print("Event day:")
print(event_time.day)

print()


# ============================================================
# 24. CREATE PARTITIONS
# ============================================================

# Very common in Data Engineering

partition_date = event_time.strftime("%Y-%m-%d")

partition_year = event_time.strftime("%Y")
partition_month = event_time.strftime("%m")
partition_day = event_time.strftime("%d")

print("Partition date:", partition_date)
print("Partition year:", partition_year)
print("Partition month:", partition_month)
print("Partition day:", partition_day)

print()


# ============================================================
# 25. CREATE A FILE PATH USING DATE
# ============================================================

file_name = f"events_{partition_date}.json"

print("File name:")
print(file_name)

print()


# ============================================================
# 26. LOGGING EXAMPLE
# ============================================================

log_time = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(f"[{log_time}] ETL pipeline started")

print()


# ============================================================
# 27. SIMPLE ETL TIMING
# ============================================================

start_time = datetime.now()

# Imagine ETL processing happens here

end_time = datetime.now()

execution_time = end_time - start_time

print("ETL execution time:")
print(execution_time)

print()


# ============================================================
# 28. COMPLETE DATA ENGINEERING EXAMPLE
# ============================================================

events = [
    {
        "id": 1,
        "timestamp": "2026-09-06 10:15:00",
        "value": 100
    },
    {
        "id": 2,
        "timestamp": "2026-09-06 11:30:00",
        "value": 200
    },
    {
        "id": 3,
        "timestamp": "2026-09-06 12:45:00",
        "value": 300
    }
]

for event in events:

    # Convert string → datetime
    event_time = datetime.strptime(
        event["timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    # Extract date information
    event["event_time"] = event_time
    event["event_date"] = event_time.strftime("%Y-%m-%d")
    event["event_year"] = event_time.year
    event["event_month"] = event_time.month
    event["event_day"] = event_time.day
    event["event_hour"] = event_time.hour

print("Transformed events:")

for event in events:
    print(event)

print()


# ============================================================
# SUMMARY
# ============================================================

# datetime.now()
#     → current date + time
#
# date.today()
#     → current date
#
# datetime(...)
#     → create specific datetime
#
# date(...)
#     → create specific date
#
# time(...)
#     → create specific time
#
# strftime(...)
#     → datetime → string
#
# strptime(...)
#     → string → datetime
#
# timedelta(...)
#     → add/subtract time
#
# datetime.date()
#     → extract date
#
# datetime.time()
#     → extract time
#
# datetime.year
# datetime.month
# datetime.day
# datetime.hour
# datetime.minute
# datetime.second
#     → extract datetime components