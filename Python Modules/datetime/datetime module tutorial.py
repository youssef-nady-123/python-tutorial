# datetime: is a built-in python module used to work with:
# - dates
# - time
# - timestamps
# - Date/Time calculations
# - Formatting and parsing dates 


# import the module, and this contains several important classes
# - date
# - time
# - timedelta 
# - timezone 
from datetime import datetime, date, time, timedelta, timezone

# -----------------
# -- for example -- 
# -----------------
# date
# 2026-09-07

# time
# 05:19:30

# datetime
# 2026-09-07 05:19:30

# timedelta
# 3 days, 2 hours
# -----------------------------------------

# get the current date and time 
now = datetime.now()
print(now)      # 2026-09-06 17:23:56.952109


# -----------------------------------
# -- extract individual components -- 
# -----------------------------------

# get the year
print(now.year)     # 2026

# get the month 
print(now.month)        # 9

# print the day 
print(now.day)          # 6

# print the hour
print(now.hour)         # 17

# print the minute
print(now.month)        # 9

# print the second
print(now.second)       # 18
# -----------------------------------------

# ----------------------------------
# -- creating a specific datetime -- 
# ----------------------------------
# datetime(year, month, day, hour, minute, second)

# create specific date & time 
dt = datetime(2026, 9, 7, 10, 30, 0)
print(dt)           # 2026-09-07 10:30:00

dt = datetime(2026, 1, 15)
print(dt)           # 2026-01-15 00:00:00


# get the current date only without time 
today = date.today()
print(today)        # 2026-09-06


# get the year, month, day on the current date
print(today.year)       # 2026
print(today.month)      # 9
print(today.day)        # 6


# ===============
# == timedelta == 
# ===============
# - timedelta: represents a duration or difference between two dates/times


# adding time 
now = datetime.now()
print(now)          # 2026-09-06 17:36:34.538854

future = now + timedelta(days=10)
print(future)       # 2026-09-16 17:36:34.538854

# -------------------------------------------

dt = datetime(2026, 9, 7, 10, 0, 0)
print(dt)           # 2026-09-07 10:00:00

new_dt = dt + timedelta(days=2)
print(new_dt)       # 2026-09-09 10:00:00


# subtract time
dt = datetime(2026, 9, 7, 10, 0, 0)

new_dt = dt - timedelta(hours=5)
print(new_dt)       # 2026-09-07 05:00:00


# check timestamp from the last 10 minutes
now = datetime.now()
ten_minutes_ago = now - timedelta(minutes=10)
print(ten_minutes_ago)      # 2026-09-06 18:42:31.673541


# =============================
# == comparing date and time == 
# =============================
dt1 = datetime(2026, 9, 7, 10, 0)
dt2 = datetime(2026, 9, 7, 12, 0)

print(dt1 < dt2)        # True 
print(dt1 > dt2)        # False
print(dt1 == dt2)       # False

# ------------------------------------------

# strftime(): format datetime as a string 
# - datetime -> string 

dt = datetime(2026, 9, 7, 10, 30, 45)
formatted = dt.strftime("%Y-%m-%d")
print(formatted)        # 2026-09-07


formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)        # 2026-09-07 10:30:45

# ============================
# == important format codes ==
# ============================
# | Code | Meaning      |
# | ---- | ------------ |
# | `%Y` | 4-digit year |
# | `%m` | month        |
# | `%d` | day          |
# | `%H` | hour         |
# | `%M` | minute       |
# | `%S` | second       |

filename = datetime.now().strftime("%Y-%m-%d")
print(f'filename: {filename}')      # filename: 2026-09-06

# ------------------------------------------------

# strptime(): convert a string into a datetime object 
# - string -> datetime 

timestamp = "2026-09-07 10:30:45"

dt = datetime.strptime(
    timestamp,
    "%Y-%m-%d %H:%M:%S"
)

print(dt)           # 2026-09-07 10:30:45
print(type(dt))     # <class 'datetime.datetime'>


dt = datetime.strptime(
    "07/09/2026 10:30:45",
    "%d/%m/%Y %H:%M:%S"
)
print(dt)           # 2026-09-07 10:30:45

# ------------------------------------------------

# timezone: this is slightly more advanced but important 
# there are two types
# 1- naive datetime
# 2- timezone-aware datetime 


# naive timezone
dt = datetime.now()
print(dt)       # 2026-09-06 19:02:42.148443

# timezone-aware datetime 
dt = datetime.now(timezone.utc)
print(dt)       # 2026-09-06 16:03:37.835429+00:00


# you can create a specific UTC datetime 
dt = datetime(
    2026,
    9,
    7,
    10,
    30,
    tzinfo=timezone.utc
)

print(dt)       # 2026-09-07 10:30:00+00:0
