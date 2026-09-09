# Build a complete Sales ETL pipeline
# Extract
# Transform
# Validate
# Load


# ============================================
# EXTRACT
# ============================================

def extract_data():
    return [
        {
            "sale_id": 1,
            "product": "Laptop",
            "quantity": 2,
            "unit_price": 25000,
            "payment": "paid"
        },
        {
            "sale_id": 2,
            "product": "Mouse",
            "quantity": 5,
            "unit_price": 500,
            "payment": "pending"
        },
        {
            "sale_id": 3,
            "product": "Keyboard",
            "quantity": 3,
            "unit_price": 1200,
            "payment": "paid"
        },
        {
            "sale_id": 4,
            "product": "Monitor",
            "quantity": 2,
            "unit_price": 7000,
            "payment": "paid"
        },
        {
            "sale_id": 5,
            "product": "Headphones",
            "quantity": 4,
            "unit_price": 2000,
            "payment": "pending"
        }
    ]


# ============================================
# TRANSFORM
# ============================================

def transform_data(sales):
    transformed_sales = []

    for sale in sales:
        new_sale = sale.copy()

        # Calculate total amount
        new_sale["total_amount"] = (
            new_sale["quantity"] * new_sale["unit_price"]
        )

        # Create sales category
        if new_sale["total_amount"] >= 5000:
            new_sale["sales_category"] = "High"
        else:
            new_sale["sales_category"] = "Normal"
        # Create payment status
        if new_sale["payment"] == "paid":
            new_sale["payment_status"] = "Completed"
        else:
            new_sale["payment_status"] = "Pending"
        transformed_sales.append(new_sale)

    return transformed_sales


# ============================================
# VALIDATE
# ============================================
def validate_data(sales):
    valid_sales = []
    for sale in sales:
        if (
            sale["sale_id"] is not None
            and sale["product"] is not None
            and sale["quantity"] is not None
            and sale["quantity"] > 0
            and sale["unit_price"] is not None
            and sale["unit_price"] >= 0
            and sale["payment"] in ["paid", "pending"]
        ):
            valid_sales.append(sale)

    return valid_sales


# ============================================
# LOAD
# ============================================
def load_data(sales):
    print("Loading sales data...")
    for sale in sales:
        print(sale)


# ============================================
# RUN ETL PIPELINE
# ============================================
raw_data = extract_data()
transformed_data = transform_data(raw_data)
valid_data = validate_data(transformed_data)
load_data(valid_data)