# Build a complete Employee ETL pipeline
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
            "employee_id": 1,
            "first_name": "Ahmed",
            "last_name": "Ali",
            "department": "Data",
            "salary": 18000,
            "status": "active"
        },
        {
            "employee_id": 2,
            "first_name": "Mohamed",
            "last_name": "Hassan",
            "department": "IT",
            "salary": 25000,
            "status": "active"
        },
        {
            "employee_id": 3,
            "first_name": "Youssef",
            "last_name": "Nady",
            "department": "Data",
            "salary": 9000,
            "status": "active"
        },
        {
            "employee_id": 4,
            "first_name": "Omar",
            "last_name": "Samir",
            "department": "HR",
            "salary": 12000,
            "status": "inactive"
        },
        {
            "employee_id": 5,
            "first_name": "Ali",
            "last_name": "Mostafa",
            "department": "Finance",
            "salary": 22000,
            "status": "active"
        }
    ]


# ============================================
# TRANSFORM
# ============================================

def transform_data(employees):
    transformed_employees = []

    for employee in employees:
        new_employee = employee.copy()

        # Create full name
        new_employee["full_name"] = (
            new_employee["first_name"]
            + " "
            + new_employee["last_name"]
        )

        # Create salary level
        if new_employee["salary"] >= 20000:
            new_employee["salary_level"] = "Senior"
        elif new_employee["salary"] >= 10000:
            new_employee["salary_level"] = "Mid"
        else:
            new_employee["salary_level"] = "Junior"

        # Create employment status
        if new_employee["status"] == "active":
            new_employee["employment_status"] = "Active"
        else:
            new_employee["employment_status"] = "Inactive"
        transformed_employees.append(new_employee)
    return transformed_employees


# ============================================
# VALIDATE
# ============================================

def validate_data(employees):
    valid_employees = []

    for employee in employees:
        if (
            employee["employee_id"] is not None
            and employee["first_name"] is not None
            and employee["last_name"] is not None
            and employee["department"] is not None
            and employee["salary"] is not None
            and employee["salary"] >= 0
            and employee["status"] in ["active", "inactive"]
        ):
            valid_employees.append(employee)
    return valid_employees


# ============================================
# LOAD
# ============================================

def load_data(employees):
    print("Loading employee data...")
    for employee in employees:
        print(employee)


# ============================================
# RUN ETL PIPELINE
# ============================================
raw_data = extract_data()
transformed_data = transform_data(raw_data)
valid_data = validate_data(transformed_data)
load_data(valid_data)
