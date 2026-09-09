#  Build a complete mini ETL pipeline
# Extract
# Transform
# Validate
# Load
def extract_data():

    return [
        {"order_id": 1, "customer": "Ahmed", "amount": 500},
        {"order_id": 2, "customer": "Mohamed", "amount": 1200},
        {"order_id": 3, "customer": "Youssef", "amount": 300},
        {"order_id": 4, "customer": "Omar", "amount": 2000},
        {"order_id": 5, "customer": "Ali", "amount": 800}
    ]


def transform_data(orders):
    transformed_orders = []

    for order in orders:
        new_order = order.copy()
        if new_order["amount"] >= 1000:
            new_order["status"] = "High"
        else:
            new_order["status"] = "Normal"
        transformed_orders.append(new_order)

    return transformed_orders


def validate_data(orders):
    valid_orders = []

    for order in orders:
        if (
            order["order_id"] is not None
            and order["customer"] is not None
            and order["amount"] is not None
            and order["amount"] >= 0
        ):
            valid_orders.append(order)
    return valid_orders


def load_data(orders):
    print("Loading data...")
    for order in orders:
        print(order)


# Run ETL Pipeline
raw_data = extract_data()
transformed_data = transform_data(raw_data)
valid_data = validate_data(transformed_data)
load_data(valid_data)