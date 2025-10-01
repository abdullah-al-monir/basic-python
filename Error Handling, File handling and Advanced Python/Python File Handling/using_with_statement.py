# The 'with' statement is the recommended way to handle files in Python.
# It automatically manages resource acquisition and release.

FILE_NAME = "config.ini"

# Setup: Create a file
with open(FILE_NAME, "w") as config_file:
    config_file.write("VERSION=1.0\n")
    config_file.write("DEBUG=True\n")

print("1. Using 'with open(...) as file_object:'")

# 1. Using 'with' for reading
with open(FILE_NAME, "r") as config_file:
    # Inside the block, the file is guaranteed to be open.
    content = config_file.read()
    print(f"Content read:\n{content.strip()}")
    
    # Check status inside the block
    print(f"Is file closed inside the 'with' block? {config_file.closed}") 

# 2. After the 'with' block, the file is automatically closed.
# The following line attempts to access the file object outside the block
# and demonstrates its closed status.
print(f"\n2. After the block, the file is closed automatically.")
# config_file variable still exists, but the file stream is closed.
print(f"Is file closed outside the 'with' block? {config_file.closed}") 

# Attempting to use the file object now will raise a ValueError.
# try:
#     content = config_file.read()
# except ValueError as e:
#     print(f"Attempt to read after close raised: {e}")