# Build a complete Customer ETL pipeline
# Extract
# Transform
# Validate
# Load


# ============================================
# EXTRACT
# ============================================

def extract_data():
    return [
        {"customer_id": 1, "name": "Ahmed", "age": 25, "total_spent": 1500},
        {"customer_id": 2, "name": "Mohamed", "age": 35, "total_spent": 5000},
        {"customer_id": 3, "name": "Youssef", "age": 19, "total_spent": 800},
        {"customer_id": 4, "name": "Omar", "age": 42, "total_spent": 12000},
        {"customer_id": 5, "name": "Ali", "age": 28, "total_spent": 3000}
    ]


# ============================================
# TRANSFORM
# ============================================

def transform_data(customers):
    transformed_customers = []

    for customer in customers:
        new_customer = customer.copy()
        # Create age_group
        if new_customer["age"] < 25:
            new_customer["age_group"] = "Young"
        elif new_customer["age"] < 40:
            new_customer["age_group"] = "Adult"
        else:
            new_customer["age_group"] = "Senior"

        # Create customer_type
        if new_customer["total_spent"] >= 5000:
            new_customer["customer_type"] = "VIP"
        else:
            new_customer["customer_type"] = "Regular"
        transformed_customers.append(new_customer)
    return transformed_customers


# ============================================
# VALIDATE
# ============================================

def validate_data(customers):
    valid_customers = []

    for customer in customers:
        if (
            customer["customer_id"] is not None
            and customer["name"] is not None
            and customer["age"] is not None
            and customer["total_spent"] is not None
            and customer["age"] >= 0
            and customer["total_spent"] >= 0
        ):
            valid_customers.append(customer)

    return valid_customers

# ============================================
# LOAD
# ============================================

def load_data(customers):
    print("Loading customer data...")
    for customer in customers:
        print(customer)


# ============================================
# RUN ETL PIPELINE
# ============================================
raw_data = extract_data()
transformed_data = transform_data(raw_data)
valid_data = validate_data(transformed_data)
load_data(valid_data)