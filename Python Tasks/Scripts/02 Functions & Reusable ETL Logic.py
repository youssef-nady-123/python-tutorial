orders = [
    {"order_id": 1, "customer": "Ahmed", "amount": 500},
    {"order_id": 2, "customer": "Mohamed", "amount": 1200},
    {"order_id": 3, "customer": "Youssef", "amount": 300},
    {"order_id": 4, "customer": "Omar", "amount": 2000},
    {"order_id": 5, "customer": "Ali", "amount": 800}
]


# TASK 1 — Create a function that prints all orders
def print_orders(orders):
    for order in orders:
        print(order)

print_orders(orders=orders)
print('='*33)


# TASK 2 — Create a function that returns customer names
def get_customer_names(orders):
    names = []

    for order in orders:
        names.append(order['customer'])

    return names

customer_names = get_customer_names(orders)
print(customer_names)
print('='*33)


# TASK 3 — Create a function that returns orders where amount > 1000
def get_high_value_orders(orders):

    high_value_orders = []

    for order in orders:
        if order['amount'] > 1000:
            high_value_orders.append(order)

    return high_value_orders

high_value_orders = get_high_value_orders(orders)
print(high_value_orders)
print('='*33)


# TASK 4 — Create a function that calculates total revenue
def calculate_total_revenue(orders):
    total = 0

    for order in orders:
        total += order['amount']

    return total

total = calculate_total_revenue(orders)
print(total)    # 4800
print('='*33)


# TASK 5 — Create a function that calculates average order value
def calculate_average_order_value(orders):
    total = 0

    for order in orders:
        total += order['amount']

    return total / len(orders)

average_order = calculate_average_order_value(orders)
print(average_order)        # 960.0
print('='*33)


# TASK 6 — Create a function that adds a status column
# amount >= 1000 → High
# amount < 1000  → Normal
def add_order_status(orders):
    for order in orders:
        if order['amount'] >= 1000:
            order['status'] = "High"
        else:
            order['status'] = "Normal"

    return orders

orders = add_order_status(orders)
print(orders)
print('='*33)


# TASK 7 — Create a function that validates orders
# An order is valid if:
# - order_id is not None
# - customer is not None
# - amount is not None
# - amount >= 0
def validate_orders(orders):
    valid_orders = []

    for order in orders:
        if (
            order['order_id'] is not None
            and order['customer'] is not None
            and order['amount'] is not None
            and order['amount'] >= 0
        ):
            valid_orders.append(order)

    return valid_orders

valid_orders = validate_orders(orders)
print(valid_orders)
print('='*33)


# TASK 8 — Create a function that calculates order count
def count_orders(orders):
    for order in orders:
        return len(orders)

order_count = count_orders(orders)
print(order_count)      # 5
print('='*33)


# TASK 9 — Create a function that finds the highest-value order
def get_highest_order(orders):
    highest_order = orders[0]

    for order in orders:
        if order['amount'] > highest_order['amount']:
            highest_order = order

    return highest_order

highest_order = get_highest_order(orders)
print(highest_order)
print('=' * 33)


# TASK 10 — Create a function that finds the lowest-value order
def get_lowest_order(orders):
    lowest_order = orders[0]

    for order in orders:
        if order['amount'] < lowest_order['amount']:
            lowest_order = order

    return lowest_order

lowest_order = get_lowest_order(orders)
print(lowest_order)
print('=' * 33)

# TASK 11 — Create a function that filters orders based on a minimum amount
# Example:
# get_orders_by_min_amount(orders, 800)
def get_orders_by_min_amount(orders, minimum_amount):
    filtered_orders = []

    for order in orders:
        if order["amount"] >= minimum_amount:
            filtered_orders.append(order)

    return filtered_orders

filtered_orders = get_orders_by_min_amount(orders, 800)
print(filtered_orders)
print('=' * 33)

# TASK 12 — Create a function that calculates total revenue for a specific status
# Example:
# calculate_revenue_by_status(orders, "High")
def calculate_revenue_by_status(orders, status):
    total = 0

    for order in orders:
        if order["status"] == status:
            total += order["amount"]

    return total

high_revenue = calculate_revenue_by_status(
    orders,
    "High"
)
print("High Revenue:", high_revenue)
print('=' * 33)

# TASK 13 — Create a reusable transformation function
# The function should:
# 1. Add status
# 2. Return the transformed dataset
def transform_orders(orders):
    transformed_orders = []

    for order in orders:
        transformed_order = order.copy()
        if transformed_order["amount"] >= 1000:
            transformed_order["status"] = "High"
        else:
            transformed_order["status"] = "Normal"
        transformed_orders.append(transformed_order)

    return transformed_orders

transformed_orders = transform_orders(orders)
print(transformed_orders)
print('=' * 33)
