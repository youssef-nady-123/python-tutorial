import json
import random

data = []

for i in range(1, 101):

    record = {
        "id": i,
        "name": f"User_{i}",
        "age": random.randint(18, 60),
        "salary": random.randint(5000, 30000),
        "department": random.choice([
            "Data Engineering",
            "IT",
            "Finance",
            "HR"
        ])
    }

    data.append(record)

with open("employees.json", "w") as file:
    json.dump(data, file, indent=4)

