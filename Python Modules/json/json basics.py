import json

# 1. JSON object
json_data = '''
{
    "id": 101,
    "name": "Youssef",
    "age": 24,
    "skills": ["Python", "SQL", "PySpark"],
    "active": true
}
'''

# 2. JSON string -> Python dictionary
data = json.loads(json_data)

print(data)
print(type(data))

# Access values
print(data["id"])
print(data["name"])
print(data["skills"])

# Access list inside JSON
print(data["skills"][0])


# 3. JSON array -> Python list
json_users = '''
[
    {"id": 1, "name": "Ahmed"},
    {"id": 2, "name": "Ali"},
    {"id": 3, "name": "Omar"}
]
'''

users = json.loads(json_users)

print(type(users))

for user in users:
    print(user["id"], user["name"])


# 4. Python dictionary -> JSON string
data = {
    "name": "Youssef",
    "age": 24,
    "skills": ["Python", "SQL"]
}

json_string = json.dumps(data, indent=4)

print(json_string)
print(type(json_string))


# 5. Safely get a value
print(data.get("name"))
print(data.get("email"))
print(data.get("email", "Not found"))


# 6. Nested JSON
response = {
    "status": "success",
    "data": {
        "user": {
            "id": 101,
            "name": "Youssef"
        }
    }
}

print(response["data"]["user"]["name"])