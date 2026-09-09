#  Build a complete Product Inventory ETL pipeline
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
            "product_id": 1,
            "product_name": "Laptop",
            "category": "Electronics",
            "quantity": 25,
            "unit_price": 25000
        },
        {
            "product_id": 2,
            "product_name": "Mouse",
            "category": "Electronics",
            "quantity": 8,
            "unit_price": 500
        },
        {
            "product_id": 3,
            "product_name": "Desk",
            "category": "Furniture",
            "quantity": 0,
            "unit_price": 7000
        },
        {
            "product_id": 4,
            "product_name": "Chair",
            "category": "Furniture",
            "quantity": 15,
            "unit_price": 3500
        },
        {
            "product_id": 5,
            "product_name": "Notebook",
            "category": "Stationery",
            "quantity": 50,
            "unit_price": 100
        }
    ]


# ============================================
# TRANSFORM
# ============================================

def transform_data(products):
    transformed_products = []

    for product in products:
        new_product = product.copy()
        # Calculate inventory value
        new_product["inventory_value"] = (
            new_product["quantity"]
            * new_product["unit_price"]
        )

        # Create stock status
        if new_product["quantity"] == 0:
            new_product["stock_status"] = "Out of Stock"
        elif new_product["quantity"] <= 10:
            new_product["stock_status"] = "Low Stock"
        else:
            new_product["stock_status"] = "In Stock"

        # Create product category
        if new_product["category"] == "Electronics":
            new_product["product_category"] = "Tech"
        elif new_product["category"] == "Furniture":
            new_product["product_category"] = "Home"
        else:
            new_product["product_category"] = "Other"
        transformed_products.append(new_product)
    return transformed_products


# ============================================
# VALIDATE
# ============================================

def validate_data(products):
    valid_products = []
    for product in products:

        if (
            product["product_id"] is not None
            and product["product_name"] is not None
            and product["category"] is not None
            and product["quantity"] is not None
            and product["quantity"] >= 0
            and product["unit_price"] is not None
            and product["unit_price"] >= 0
        ):
            valid_products.append(product)
    return valid_products


# ============================================
# LOAD
# ============================================

def load_data(products):
    print("Loading inventory data...")
    for product in products:
        print(product)


# ============================================
# RUN ETL PIPELINE
# ============================================
raw_data = extract_data()
transformed_data = transform_data(raw_data)
valid_data = validate_data(transformed_data)
load_data(valid_data)
