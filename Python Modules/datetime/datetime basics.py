import datetime


# ==========================================
# date.today()
# Get today's date
# ==========================================

# Get today's date
print(datetime.date.today())


# ==========================================
# datetime.now()
# Get the current date and time
# ==========================================

# Get the current date and time
print(datetime.datetime.now())


# ==========================================
# Create a specific date and time
# ==========================================

# Create a datetime object:
# Year = 2026
# Month = 1
# Day = 15
# Hour = 10
# Minute = 30
# Second = 0
dt = datetime.datetime(2026, 1, 15, 10, 30, 0)

# Print the datetime object
print(dt)


# ==========================================
# timedelta()
# Calculate a date/time in the past
# ==========================================

# Get the current date and time
now = datetime.datetime.now()

# Create a timedelta object representing 7 days
seven_days = datetime.timedelta(days=7)

# Subtract 7 days from the current date and time
dt = now - seven_days

# Print the current date and time
print(now)

# Print the timedelta object
print(seven_days)

# Print the date/time from 7 days ago
print(dt)


# ==========================================
# Get yesterday
# ==========================================

# Get today's date
today = datetime.date.today()

# Subtract 1 day from today
yesterday = today - datetime.timedelta(days=1)

# Print today's date
print(today)

# Print yesterday's date
print(yesterday)


# ==========================================
# Get 7 days ago
# ==========================================

# Subtract 7 days from today's date
seven_days_ago = today - datetime.timedelta(days=7)

# Print the date from 7 days ago
print(seven_days_ago)


# ==========================================
# Get 30 days ago
# ==========================================

# Subtract 30 days from today's date
days_30_ago = today - datetime.timedelta(days=30)

# Print the date from 30 days ago
print(days_30_ago)


# ==========================================
# strftime()
# Convert datetime/date object -> string
# ==========================================

# Get the current date and time
now = datetime.datetime.now()


# Convert datetime object to a string
# %Y = 4-digit year
# %m = month
# %d = day
formatted_date = now.strftime("%Y-%m-%d")

# Print the formatted date
print(formatted_date)


# Convert datetime object to a string
# %H = hour
# %M = minute
# %S = second
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date and time
print(formatted_datetime)


# Convert datetime object to DD/MM/YYYY format
formatted_date_2 = now.strftime("%d/%m/%Y")

# Print the formatted date
print(formatted_date_2)


# Convert datetime object to:
# Month Day, Year
# Example: September 09, 2026
# %B = full month name
formatted_date_3 = now.strftime("%B %d, %Y")

# Print the formatted date
print(formatted_date_3)


# ==========================================
# strptime()
# Convert string -> datetime object
# ==========================================

# Store a date/time as a string
date_string = "2026-01-15 10:30:00"


# Convert the string into a datetime object
#
# The format must match the string:
# %Y = 4-digit year
# %m = month
# %d = day
# %H = hour
# %M = minute
# %S = second
dt = datetime.datetime.strptime(
    date_string,
    "%Y-%m-%d %H:%M:%S"
)

# Print the datetime object
print(dt)

# Check the data type
print(type(dt))


# ==========================================
# Another strptime() example
# ==========================================

# Store a date as a string
date_string = "15/01/2026"


# Convert the string into a datetime object
#
# The format matches the string:
# %d = day
# %m = month
# %Y = 4-digit year
dt = datetime.datetime.strptime(
    date_string,
    "%d/%m/%Y"
)

# Print the datetime object
print(dt)

# Check the data type
print(type(dt))
