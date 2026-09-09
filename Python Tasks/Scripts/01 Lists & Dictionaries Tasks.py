orders = [
    {"order_id": 1, "customer": "Ahmed", "amount": 500},
    {"order_id": 2, "customer": "Mohamed", "amount": 1200},
    {"order_id": 3, "customer": "Youssef", "amount": 300},
    {"order_id": 4, "customer": "Omar", "amount": 2000},
    {"order_id": 5, "customer": "Ali", "amount": 800}
]


# TASK 1 — Print every order
for order in orders:
    print(order)
print('='*33)


# TASK 2 — Print only the customer names
for order in orders:
    print(order['customer'])
print('='*33)


# TASK 3 — Print orders where amount > 1000
for order in orders:
    if order['amount'] > 1000:
        print(order['amount'])
print('='*33)


# TASK 4 — Calculate the total order amount
total_amount = 0 

for order in orders:
    total_amount += order['amount']

print(f'total amounts: {total_amount}')     # total amounts: 4800
print('='*33)



# TASK 5 — Calculate the average order amount
total_amount = 0

for order in orders:
    total_amount += order['amount']

average_order_amount = total_amount / len(orders)
print(average_order_amount)     # 960.0
print('='*33)



# TASK 6 — Create a list containing only orders greater than 500
orders_greater_than_500 = []

for order in orders:
    if order['amount'] > 500:
        orders_greater_than_500.append(order)

print(orders_greater_than_500)
print('='*33)


# TASK 7 — Add a "status" field to every order
# amount >= 1000 → "High"
# amount < 1000  → "Normal"
for order in orders:
    if order['amount'] >= 1000 :
        order['status'] = "High"
    else:
        order['status'] = "Normal"

for order in orders:
    print(order)
print('='*33)


# TASK 8 — Get only the names of High-value customers
high_value_customers = []

for order in orders:
    if order['status'] == "High":
        high_value_customers.append(order['customer'])

print(high_value_customers)
print('='*33)


# TASK 9 — Calculate total revenue from High-value orders
high_value_revenue = 0 

for order in orders:
    if order['status'] == "High":
        high_value_revenue += order['amount']

print(high_value_revenue)       # 3200
print('='*33)


# TASK 10 — Find the order with the highest amount
highest_order  = orders[0]

for order in orders:
    if order['amount'] > highest_order ['amount']:
        highest_order = order

print(highest_order)    # {'order_id': 4, 'customer': 'Omar', 'amount': 2000, 'status': 'High'}
print('='*33)


# TASK 11 — Find the order with the lowest amount
lowest_order = orders[0]

for order in orders:
    if order['amount'] < lowest_order['amount']:
        lowest_order = order

print(lowest_order)     # {'order_id': 3, 'customer': 'Youssef', 'amount': 300, 'status': 'Normal'}
print('='*33)


# TASK 12 Create a list of customer names using list comprehension 
customer_names = [
    order['customer']
    for order in orders
]

print(customer_names)       # ['Ahmed', 'Mohamed', 'Youssef', 'Omar', 'Ali']
print('='*33)



# TASK 13 — Create a list containing only the order amounts
order_amounts = [
    order['amount']
    for order in orders
]

print(order_amounts)    # [500, 1200, 300, 2000, 800]
print('='*33)



# TASK 14 — Calculate total using sum()
total_sum = sum(
    order['amount']
    for order in orders
)

print(total_sum)        # 4800
print('='*33)


# TASK 15 — Calculate average using sum() and len()
average_amount = (
    sum(order['amount'] for order in orders) / len(orders)
)

print(average_amount)       # 960.0
print('='*33)


# TASK 16 — Count High and Normal orders
high_count = 0 
normal_count = 0

for order in orders:
    if order['status'] == "High":
        high_count += 1 
    else:
        normal_count += 1

print(f"high orders: {high_count}")     # high orders: 2
print(f"normal orders: {normal_count}")     # normal orders: 3
print('='*33)

# TASK 17 — Create a dictionary containing summary information
summary = {
    "total_orders": len(orders),
    "total_revenue": sum(order['amount'] for order in orders),
    "average_order": sum(order['amount'] for order in orders) / len(orders),
    "high_value_order": high_count,
    "normal_orders": normal_count
}
print(summary)
print('='*33)


# TASK 18 — Data Engineering Transformation
# Create a new dataset containing:
# order_id
# customer
# amount
# status
# Do not modify the original dataset.
transformed_orders = []

for order in orders:
    transformed_order = {
        "order_id": order['order_id'],
        "customer": order["customer"],
        "amount": order['amount'],
        "status": order['status']
    }

    transformed_orders.append(transformed_order)

print(transformed_orders)
print('='*33)