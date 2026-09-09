import json
import random
import time
from datetime import datetime, timezone


def generate_event():
    return {
        "id": random.randint(1, 100000),
        "name": random.choice(["Ali", "Omar", "Youssef", "Ahmed"]),
        "category": random.choice(["electronics", "clothing", "food"]),
        "value": round(random.uniform(10, 1000), 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


batch_number = 1

while True:

    events = []

    # Generate 10 fake events
    for _ in range(10):
        events.append(generate_event())

    # Create filename
    filename = f"batch_{batch_number:03d}.json"

    # Write events to JSON file
    with open(filename, "w") as file:
        json.dump(events, file, indent=4)

    print(f"Created: {filename}")

    batch_number += 1

    # Wait 1 minute
    time.sleep(60)