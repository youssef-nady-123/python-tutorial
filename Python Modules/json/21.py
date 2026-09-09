import json
import random

transactions = []

for i in range(1, 101):

    transaction = {
        "transaction_id": i,
        "customer_id": random.randint(1, 20),
        "amount": round(random.uniform(10, 1000), 2),
        "category": random.choice([
            "Electronics",
            "Clothing",
            "Food",
            "Books"
        ]),
        "status": random.choice([
            "completed",
            "pending",
            "cancelled"
        ])
    }

    transactions.append(transaction)

with open("transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)
