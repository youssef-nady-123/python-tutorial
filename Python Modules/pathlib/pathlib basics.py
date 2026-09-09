from pathlib import Path

# ==========================================
# 1. Current working directory
# ==========================================

current_dir = Path.cwd()
print("Current directory:", current_dir)


# ==========================================
# 2. Create paths
# ==========================================

project_dir = Path("api_project")
data_dir = project_dir / "data"
raw_dir = data_dir / "raw"
processed_dir = data_dir / "processed"
json_dir = raw_dir / "json"

print("\nPaths:")
print(project_dir)
print(data_dir)
print(raw_dir)
print(processed_dir)
print(json_dir)


# ==========================================
# 3. Create directories
# ==========================================

json_dir.mkdir(parents=True, exist_ok=True)
processed_dir.mkdir(parents=True, exist_ok=True)

print("\nDirectories created.")


# ==========================================
# 4. Check if path exists
# ==========================================

print("\nExists:")
print("Project:", project_dir.exists())
print("Raw:", raw_dir.exists())
print("JSON:", json_dir.exists())


# ==========================================
# 5. Create a file
# ==========================================

file = json_dir / "test.json"

file.touch()

print("\nFile created:", file)


# ==========================================
# 6. Write to a file
# ==========================================

file.write_text('{"id": 1, "name": "Youssef"}')

print("\nFile content written.")


# ==========================================
# 7. Read from a file
# ==========================================

content = file.read_text()

print("\nFile content:")
print(content)


# ==========================================
# 8. Check file information
# ==========================================

print("\nFile information:")
print("Exists:", file.exists())
print("Is file:", file.is_file())
print("Is directory:", file.is_dir())
print("Name:", file.name)
print("Suffix:", file.suffix)
print("Parent:", file.parent)


# ==========================================
# 9. List directory contents
# ==========================================

print("\nJSON directory contents:")

for item in json_dir.iterdir():
    print(item)


# ==========================================
# 10. Find JSON files
# ==========================================

print("\nJSON files:")

for json_file in json_dir.glob("*.json"):
    print(json_file)