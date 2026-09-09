import json
import random

response = {
    "status": "success",
    "data": []
}

for i in range(1, 11):

    customer = {
        "id": i,
        "name": f"Customer_{i}",
        "address": {
            "city": random.choice(["Cairo", "Giza", "Alexandria"]),
            "country": "Egypt"
        },
        "orders": [
            {
                "order_id": i * 100,
                "amount": round(random.uniform(100, 2000), 2)
            }
        ]
    }

    response["data"].append(customer)

with open("api_response.json", "w") as file:
    json.dump(response, file, indent=4)