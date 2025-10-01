# Demonstrates the full try-except-else-finally control flow.

def process_file_operation(filename, operation):
    """Simulates a file operation, demonstrating all four keywords."""
    file_handle = None
    try:
        # 1. try: Code block with risky operation
        # This will fail on the first run (file not found)
        # Assuming 'data.txt' exists for the else block to run on a successful test
        file_handle = open(filename, operation)
        data = file_handle.read()
        print(f"Read successful. Content length: {len(data)}")
        
    except FileNotFoundError:
        # 2. except: Handles the specific exception
        print("Exception: The file was not found on the system.")
        
    except AttributeError:
        # Handles case where file_handle is None and we try to call .read()
        print("Exception: Could not read data (file handle issue).")
        
    else:
        # 3. else: Executes ONLY if the try block succeeds (no exceptions)
        print("Success: The file operation completed without errors.")
        
    finally:
        # 4. finally: ALWAYS executes, regardless of success or failure
        if file_handle:
            file_handle.close()
            print("Cleanup: File handle closed.")
        print("--- Operation Complete ---")

# Test 1: File not found (triggers except and finally)
print("--- Scenario 1: File Not Found ---")
process_file_operation("non_existent_file.txt", "r")

# Test 2: Assuming 'test_data.txt' exists (triggers try, else, and finally)
# Note: For this to work in a real environment, you'd need a file named 'test_data.txt'.
print("\n--- Scenario 2: File Found (Hypothetical Success) ---")
# Simulating success by passing an invalid 'open' operation which fails try, 
# but for a true 'else' test, the open() must succeed.
# process_file_operation("test_data.txt", "r") # Use this line if file exists
print("Simulating result of a successful file read.")
print("Success: The file operation completed without errors.")
print("Cleanup: File handle closed.")
print("--- Operation Complete ---")