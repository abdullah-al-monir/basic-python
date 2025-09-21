# -----------------------------------------------------------------------------
# File: nested_dictionaries.py
# Description: Demonstrates working with dictionaries inside other dictionaries.
# -----------------------------------------------------------------------------

# Creating a nested dictionary for employee records
employees = {
    "employee_1": {
        "name": "Jane Smith",
        "age": 32,
        "department": "IT"
    },
    "employee_2": {
        "name": "John Doe",
        "age": 45,
        "department": "Finance"
    }
}
print(f"Initial nested dictionary: {employees}")

# Accessing elements in a nested dictionary
# Access the outer key, then the inner key.
print(f"\nAccessing Jane's name: {employees['employee_1']['name']}")
print(f"Accessing John's department: {employees['employee_2']['department']}")

# Adding a new key-value pair to an inner dictionary
employees['employee_1']['role'] = 'Developer'
print(f"\nAfter adding a new role: {employees}")

# Adding a new inner dictionary (a new employee)
employees['employee_3'] = {
    "name": "Peter Jones",
    "age": 28,
    "department": "Marketing"
}
print(f"After adding a new employee: {employees}")

# Deleting a key from an inner dictionary
del employees['employee_1']['department']
print(f"\nAfter deleting a department: {employees}")

# Deleting an entire inner dictionary
del employees['employee_2']
print(f"After deleting an entire employee record: {employees}")
