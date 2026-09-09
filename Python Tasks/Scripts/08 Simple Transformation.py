# Create a reusable transformation function that 
# adds status, cleans customer names, calculates tax, discount, final amount, and amount category, then returns the transformed dataset.

orders = [
    {'order_id': 1, 'customer': 'Ahmed', 'amount': 500},
    {'order_id': 2, 'customer': 'Mohamed', 'amount': 1200},
    {'order_id': 3, 'customer': 'Youssef', 'amount': 300},
    {'order_id': 4, 'customer': 'Omar', 'amount': 2000},
    {'order_id': 5, 'customer': 'Ali', 'amount': 800}
]


def transform_orders(orders):
    transformed_orders = []

    for order in orders:
        # Create a new record
        new_order = order.copy()

        # 1. Add status
        if new_order['amount'] >= 1000:
            new_order['status'] = "High"
        else:
            new_order['status'] = "Normal"

        # 2. Clean customer name
        new_order['customer'] = new_order['customer'].strip()

        # 3. Add uppercase customer name
        new_order['customer_upper'] = new_order['customer'].upper()

        # 4. Add tax
        new_order['tax'] = new_order['amount'] * 0.14

        # 5. Add amount with tax
        new_order['amount_with_tax'] = (
            new_order['amount'] + new_order['tax']
        )

        # 6. Add discount
        if new_order['amount'] >= 1500:
            new_order['discount'] = new_order['amount'] * 0.10
        elif new_order['amount'] >= 1000:
            new_order['discount'] = new_order['amount'] * 0.05
        else:
            new_order['discount'] = 0

        # 7. Calculate final amount
        new_order['final_amount'] = (
            new_order['amount']
            + new_order['tax']
            - new_order['discount']
        )

        # 8. Add amount category
        if new_order['amount'] < 500:
            new_order['amount_category'] = "Low"
        elif new_order['amount'] < 1000:
            new_order['amount_category'] = "Medium"
        else:
            new_order['amount_category'] = "High"

        # Add transformed record
        transformed_orders.append(new_order)
    return transformed_orders


transformed_orders = transform_orders(orders)

print(transformed_orders)