# Demonstrates how to open a file with specific modes and close it manually.

FILE_NAME = "data_log.txt"

# Create a dummy file for demonstration (in write mode)
with open(FILE_NAME, "w") as f:
    f.write("Initial log entry.\n")

# 1. Opening a file in read mode ('r')
# The file object is assigned to the variable 'log_file'
log_file = open(FILE_NAME, "r")
print(f"1. File '{FILE_NAME}' opened successfully.")

# 2. Checking File Properties
print("-" * 30)
print(f"Filename: {log_file.name}")
print(f"Mode: {log_file.mode}")
print(f"Is Closed (Before close)? {log_file.closed}")

# 3. Manually Closing the File
# This releases system resources and ensures data integrity.
log_file.close()
print("-" * 30)
print(f"3. File closed manually.")
print(f"Is Closed (After close)? {log_file.closed}")

# Note: Attempting to read/write after closing will raise a ValueError.