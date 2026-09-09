# ============================================================
# PYTHON OS MODULE — COMPLETE PRACTICE SCRIPT
# ============================================================

import os


# TASK 1 — Get Current Working Directory
# os.getcwd() returns the folder where your Python script
# is currently running.

current_directory = os.getcwd()

print("Current Working Directory:")
print(current_directory)

print("=" * 50)


# TASK 2 — Change Working Directory
# os.chdir() changes the current working directory.

# Example:
# os.chdir("C:\\Users\\Youssef\\Desktop")

# After changing directory:
# print(os.getcwd())

# We will not execute it here because the path
# depends on your computer.

print("Example:")
print(r'os.chdir("C:\\Users\\Youssef\\Desktop")')

print("=" * 50)


# TASK 3 — List Files and Folders
# os.listdir() returns files and folders inside a directory.

items = os.listdir(".")

print("Files and folders:")
print(items)

print("=" * 50)


# TASK 4 — Check If a File Exists
# os.path.exists() checks whether a file or folder exists.

file_path = "data.txt"

if os.path.exists(file_path):
    print("data.txt exists")
else:
    print("data.txt does not exist")

print("=" * 50)


# TASK 5 — Check If Path Is a File

if os.path.isfile("data.txt"):
    print("data.txt is a file")
else:
    print("data.txt is not a file")

print("=" * 50)


# TASK 6 — Check If Path Is a Directory

if os.path.isdir("data"):
    print("data is a directory")
else:
    print("data is not a directory")

print("=" * 50)


# TASK 7 — Create a Directory

# os.mkdir() creates ONE directory.

# Example:
# os.mkdir("data")

# If "data" already exists, this will cause an error.

print("Example:")
print('os.mkdir("data")')

print("=" * 50)


# TASK 8 — Create Nested Directories

# os.makedirs() can create multiple directories.

# Example:
#
# data/
#     raw/
#         csv/
#
# os.makedirs("data/raw/csv")

print("Example:")
print('os.makedirs("data/raw/csv")')

print("=" * 50)

# TASK 9 — Create Directory Only If It Does Not Exist

# exist_ok=True prevents an error if the directory
# already exists.

os.makedirs("example_data/raw", exist_ok=True)

print("Directory created:")
print("example_data/raw")

print("=" * 50)


# TASK 10 — Create a File

# We can use Python's open() function to create a file.

with open("example_data/data.txt", "w") as file:
    file.write("Hello Data Engineering!")

print("data.txt created")

print("=" * 50)


# TASK 11 — List Files Inside a Directory

items = os.listdir("example_data")

print("Items inside example_data:")

for item in items:
    print(item)

print("=" * 50)


# TASK 12 — Build File Paths
# NEVER depend on manually writing:
#
# "data/raw/file.csv"
#
# Instead, os.path.join() builds paths correctly
# for the operating system.

folder = "data"
subfolder = "raw"
filename = "customers.csv"

path = os.path.join(folder, subfolder, filename)

print("Built path:")
print(path)

print("=" * 50)


# TASK 13 — Get File Name From Path

path = "data/raw/customers.csv"

filename = os.path.basename(path)

print("File name:")
print(filename)

print("=" * 50)


# TASK 14 — Get Directory From Path

directory = os.path.dirname(path)

print("Directory:")
print(directory)

print("=" * 50)


# TASK 15 — Split File Extension
# os.path.splitext() separates:
#
# customers.csv
#
# into:
#
# customers
# .csv

filename, extension = os.path.splitext("customers.csv")
print("File name:", filename)
print("Extension:", extension)

print("=" * 50)


# TASK 16 — Get Absolute Path

relative_path = "example_data/data.txt"

absolute_path = os.path.abspath(relative_path)

print("Relative path:")
print(relative_path)

print("Absolute path:")
print(absolute_path)

print("=" * 50)


# TASK 17 — Get File Size

file_size = os.path.getsize("example_data/data.txt")

print("File size:")
print(file_size, "bytes")

print("=" * 50)


# TASK 18 — Rename a File

# os.rename(old_name, new_name)

# Example:
#
# os.rename(
#     "example_data/data.txt",
#     "example_data/customers.txt"
# )

print("Example:")
print('os.rename("example_data/data.txt", "example_data/customers.txt")')

print("=" * 50)


# TASK 19 — Delete a File

# os.remove() deletes a file.

# Example:
#
# os.remove("example_data/data.txt")

print("Example:")
print('os.remove("example_data/data.txt")')

print("=" * 50)


# TASK 20 — Remove an Empty Directory

# os.rmdir() removes an EMPTY directory.

# Example:
#
# os.rmdir("example_data/raw")

print("Example:")
print('os.rmdir("example_data/raw")')

print("=" * 50)


# TASK 21 — Environment Variables
# Environment variables store configuration values
# outside your Python code.

# os.environ gives access to environment variables.

print("Some environment variables:")

for key, value in list(os.environ.items())[:5]:
    print(key, "=", value)

print("=" * 50)


# TASK 22 — Read an Environment Variable
# os.getenv() safely reads an environment variable.

username = os.getenv("USERNAME")

print("Username:")
print(username)

print("=" * 50)


# TASK 23 — Environment Variable With Default Value
# If the variable doesn't exist,
# the default value will be returned.

environment = os.getenv("ENVIRONMENT", "development")

print("Environment:")
print(environment)

print("=" * 50)


# TASK 24 — OS Name
# os.name tells us the operating-system family.

print("OS name:")
print(os.name)

# Windows -> nt
# Linux   -> posix

print("=" * 50)


# TASK 25 — Walk Through a Directory
# os.walk() is VERY useful in Data Engineering.
#
# It recursively goes through directories and files.

for root, directories, files in os.walk("example_data"):

    print("ROOT:")
    print(root)

    print("DIRECTORIES:")
    print(directories)

    print("FILES:")
    print(files)

    print("-" * 30)

print("=" * 50)


# TASK 26 — Find All CSV Files
# os.walk() can be used to find specific files.

for root, directories, files in os.walk("."):

    for file in files:

        if file.endswith(".csv"):
            print("CSV file found:")
            print(os.path.join(root, file))

print("=" * 50)


# TASK 27 — Data Engineering Example
# Imagine a typical Data Engineering project:

#
# project/
#     data/
#         raw/
#         processed/
#         archive/
#

base_directory = "project"

raw_directory = os.path.join(base_directory, "data", "raw")
processed_directory = os.path.join(base_directory, "data", "processed")
archive_directory = os.path.join(base_directory, "data", "archive")

os.makedirs(raw_directory, exist_ok=True)
os.makedirs(processed_directory, exist_ok=True)
os.makedirs(archive_directory, exist_ok=True)

print("Data Engineering directories created:")

print(raw_directory)
print(processed_directory)
print(archive_directory)

print("=" * 50)


# TASK 28 — Find Files in Raw Data
# This is a common ETL pattern.

for root, directories, files in os.walk(raw_directory):

    for file in files:

        full_path = os.path.join(root, file)

        print("Raw file:")
        print(full_path)

print("=" * 50)


# TASK 29 — Simple ETL File Organization
# Example:
#
# raw/customers.csv
#
# could eventually be moved to:
#
# processed/customers.csv
#
# using os.rename().

source = os.path.join(raw_directory, "customers.csv")
destination = os.path.join(processed_directory, "customers.csv")

print("Source:")
print(source)

print("Destination:")
print(destination)

# Actual move:
#
# os.rename(source, destination)

print("=" * 50)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("""
IMPORTANT os MODULE FUNCTIONS

os.getcwd()
    -> Get current working directory

os.chdir()
    -> Change working directory

os.listdir()
    -> List files and folders

os.path.exists()
    -> Check whether path exists

os.path.isfile()
    -> Check whether path is a file

os.path.isdir()
    -> Check whether path is a directory

os.mkdir()
    -> Create one directory

os.makedirs()
    -> Create nested directories

os.path.join()
    -> Build paths

os.path.basename()
    -> Get file name

os.path.dirname()
    -> Get directory

os.path.splitext()
    -> Get file name and extension

os.path.abspath()
    -> Get absolute path

os.path.getsize()
    -> Get file size

os.rename()
    -> Rename / move files

os.remove()
    -> Delete files

os.rmdir()
    -> Delete empty directory

os.getenv()
    -> Read environment variable

os.environ
    -> Access environment variables

os.walk()
    -> Recursively traverse directories
""")