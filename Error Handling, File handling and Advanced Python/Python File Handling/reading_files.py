# Demonstrates different methods for reading data from a file.

FILE_NAME = "inventory.csv"

# Setup: Create a file with multiple lines
file_content = """Item,Quantity,Price
Keyboard,10,50.00
Mouse,25,15.50
Monitor,5,150.00"""
with open(FILE_NAME, "w") as f:
    f.write(file_content)

# 1. Reading the entire content at once (.read())
print("--- 1. Using .read() (reads everything) ---")
with open(FILE_NAME, "r") as f:
    full_content = f.read()
    print(full_content)

# 2. Reading line by line (.readline())
print("\n--- 2. Using .readline() (reads one line at a time) ---")
with open(FILE_NAME, "r") as f:
    header = f.readline().strip()
    first_item = f.readline().strip()
    print(f"Header: {header}")
    print(f"First Item: {first_item}")

# 3. Reading all lines into a list (.readlines())
print("\n--- 3. Using .readlines() (reads all lines into a list) ---")
with open(FILE_NAME, "r") as f:
    all_lines = f.readlines()
    print(f"Total lines read: {len(all_lines)}")
    print(f"List of lines (with newlines): {all_lines[:2]}")