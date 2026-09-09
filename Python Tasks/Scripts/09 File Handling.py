# ============================================================
# PYTHON FILE HANDLING
# Data Engineering Practice
# ============================================================

# ============================================================
# 1. OPENING A FILE
# ============================================================
# Python uses open() to work with files.
# Syntax:
# open(file_path, mode)
# Common modes:
#
# "r"  -> Read
# "w"  -> Write
# "a"  -> Append
# "x"  -> Create a new file
# Example:
# file = open("data.txt", "r")
# Always close the file:
# file.close()


# ============================================================
# 2. WRITE TO A FILE
# ============================================================
# "w" means write.
# If the file does not exist:
#     Python creates it.
# If the file already exists:
#     Python overwrites it.

file = open("data.txt", "w")
file.write("Ahmed,500\n")
file.write("Mohamed,1200\n")
file.write("Youssef,750\n")
file.close()


# ============================================================
# 3. READ THE ENTIRE FILE
# ============================================================
file = open("data.txt", "r")
data = file.read()
file.close()
print("FILE CONTENT:")
print(data)

print("=" * 50)


# ============================================================
# 4. READ FILE LINE BY LINE
# ============================================================
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()

print("=" * 50)


# ============================================================
# 5. readlines()
# ============================================================
# readlines() returns all lines as a list.
file = open("data.txt", "r")
lines = file.readlines()
file.close()
print(lines)

print("=" * 50)


# ============================================================
# 6. USING with open()
# ============================================================
# Recommended approach:
# with open(...) as file:
# Python automatically closes the file.

with open("data.txt", "r") as file:
    data = file.read()
print(data)

print("=" * 50)


# ============================================================
# 7. APPEND TO A FILE
# ============================================================
# "a" means append.
# It adds new data without deleting existing data.
with open("data.txt", "a") as file:
    file.write("Sara,900\n")
    file.write("Omar,1500\n")


# Check the file
with open("data.txt", "r") as file:
    print(file.read())

print("=" * 50)


# ============================================================
# 8. HANDLE FILE NOT FOUND
# ============================================================

try:
    with open("missing.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File does not exist")

print("=" * 50)


# ============================================================
# 9. FILE HANDLING WITH EXCEPTION HANDLING
# ============================================================

try:
    with open("data.txt", "r") as file:
        data = file.read()
        print("Successfully read file")
        print(data)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

print("=" * 50)


# ============================================================
# 10. PROCESS FILE DATA
# ============================================================
# Suppose the file contains:
#
# Ahmed,500
# Mohamed,1200
# Youssef,750
#
# We can read and transform the data.

with open("data.txt", "r") as file:

    for line in file:

        line = line.strip()

        name, amount = line.split(",")

        amount = float(amount)

        print({
            "name": name,
            "amount": amount
        })

print("=" * 50)


# ============================================================
# 11. FILE HANDLING AS ETL
# ============================================================

# EXTRACT
# Read raw data from a file.
#
# TRANSFORM
# Convert amount to float.
#
# VALIDATE
# Reject invalid or negative amounts.
#
# LOAD
# Write valid records to another file.


# EXTRACT
with open("data.txt", "r") as file:
    lines = file.readlines()


# TRANSFORM + VALIDATE
valid_orders = []
rejected_orders = []

for line in lines:

    try:
        line = line.strip()
        name, amount = line.split(",")
        amount = float(amount)

        if amount < 0:
            raise ValueError("Negative amount")
        valid_orders.append({
            "name": name,
            "amount": amount
        })

    except ValueError as e:
        rejected_orders.append({
            "raw_data": line,
            "error": str(e)
        })


# LOAD VALID DATA
with open("valid_orders.txt", "w") as file:
    for order in valid_orders:
        file.write(
            f"{order['name']},{order['amount']}\n"
        )


# LOAD REJECTED DATA
with open("rejected_orders.txt", "w") as file:
    for order in rejected_orders:
        file.write(
            f"{order['raw_data']} | {order['error']}\n"
        )


# DISPLAY RESULTS
print("VALID ORDERS:")
for order in valid_orders:
    print(order)

print("\nREJECTED ORDERS:")

for order in rejected_orders:
    print(order)
print("=" * 50)


# ============================================================
# 12. CHECK FILE EXISTENCE WITH os
# ============================================================

import os
if os.path.exists("data.txt"):
    print("data.txt exists")
else:
    print("data.txt does not exist")


# Check file size
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print("File size:", size, "bytes")

print("=" * 50)


# ============================================================
# 13. DELETE A FILE
# ============================================================

# WARNING:
# This permanently deletes the file.

# if os.path.exists("data.txt"):
#     os.remove("data.txt")


# ============================================================
# 14. pathlib — MODERN FILE HANDLING
# ============================================================

from pathlib import Path

file_path = Path("data.txt")

if file_path.exists():
    print("File exists")
    print("File name:", file_path.name)
    print("File extension:", file_path.suffix)
    print("File size:", file_path.stat().st_size)


# Read using pathlib

if file_path.exists():
    data = file_path.read_text()
    print(data)


# Write using pathlib

output_path = Path("output.txt")

output_path.write_text(
    "Data Engineering\n"
    "Python File Handling\n"
)


# ============================================================
# 15. DATA ENGINEERING EXAMPLE
# ============================================================

# Raw file:
#
# orders_raw.txt
#
# 1,Ahmed,500
# 2,Mohamed,1200
# 3,Youssef,abc
# 4,Sara,-100
# 5,Omar,750
#
# Goal:
#
# Raw Data
#     ↓
# Extract
#     ↓
# Transform
#     ↓
# Validate
#     ↓
# Valid Data + Rejected Data


# Create raw input file
with open("orders_raw.txt", "w") as file:
    file.write("1,Ahmed,500\n")
    file.write("2,Mohamed,1200\n")
    file.write("3,Youssef,abc\n")
    file.write("4,Sara,-100\n")
    file.write("5,Omar,750\n")


# EXTRACT
with open("orders_raw.txt", "r") as file:

    lines = file.readlines()


# TRANSFORM + VALIDATE
valid_orders = []
rejected_orders = []


for line in lines:

    try:
        line = line.strip()
        order_id, customer, amount = line.split(",")
        order_id = int(order_id)
        amount = float(amount)

        if amount < 0:
            raise ValueError(
                "Amount cannot be negative"
            )

        valid_orders.append({
            "order_id": order_id,
            "customer": customer,
            "amount": amount
        })

    except ValueError as e:
        rejected_orders.append({
            "raw_data": line,
            "error": str(e)
        })


# LOAD VALID DATA
with open("orders_clean.txt", "w") as file:

    for order in valid_orders:

        file.write(
            f"{order['order_id']},"
            f"{order['customer']},"
            f"{order['amount']}\n"
        )


# LOAD REJECTED DATA
with open("orders_rejected.txt", "w") as file:

    for order in rejected_orders:

        file.write(
            f"{order['raw_data']} | "
            f"{order['error']}\n"
        )


# RESULTS
print("\nCLEAN ORDERS:")

for order in valid_orders:

    print(order)


print("\nREJECTED ORDERS:")

for order in rejected_orders:

    print(order)


# ============================================================
# IMPORTANT FILE HANDLING CONCEPTS
# ============================================================

# open()
# with open()
# read()
# readline()
# readlines()
# write()
# append mode "a"
# write mode "w"
# read mode "r"
# FileNotFoundError
# PermissionError
# os.path.exists()
# os.path.getsize()
# os.remove()
# pathlib.Path
# Path.read_text()
# Path.write_text()


# ============================================================
# DATA ENGINEERING CONNECTION
# ============================================================

# File
#   ↓
# Extract
#   ↓
# Validate
#   ↓
# Transform
#   ↓
# Clean File
#   ↓
# Data Warehouse / Database / Data Lake