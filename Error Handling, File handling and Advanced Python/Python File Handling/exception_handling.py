# Ensures file closing even if an error occurs during processing, using the try-finally structure.

def process_data(input_file_name):
    """Attempts to open and process a file, ensuring it closes regardless of errors."""
    file_handle = None # Initialize to None in case open() fails
    
    try:
        # 1. Risky operation: opening the file
        file_handle = open(input_file_name, "r")
        
        # 2. Risky operation: reading and processing
        content = file_handle.read()
        
        # 3. Intentional Error: Simulating a processing crash (e.g., trying to divide by zero)
        if "force_error" in content:
            print("Processing data... (forcing a crash)")
            result = 100 / 0 # This will raise a ZeroDivisionError
            
        print("Data processed successfully.")
        
    except FileNotFoundError:
        print(f"Error Handled: File '{input_file_name}' not found.")
        
    except ZeroDivisionError:
        print("Error Handled: A critical processing error occurred.")
        
    finally:
        # 4. finally: Guarantees cleanup runs, whether 'try' succeeded or 'except' handled an error
        if file_handle is not None:
            file_handle.close()
            print(f"Cleanup: File '{input_file_name}' closed in finally block.")
        else:
            print("Cleanup: No file was successfully opened.")


# Setup: Create a file that will cause an error
with open("error_test.txt", "w") as f:
    f.write("force_error")

# Test 1: Triggers an internal error (ZeroDivisionError)
print("--- Scenario 1: Internal Processing Crash ---")
process_data("error_test.txt")

# Test 2: Triggers a FileNotFoundError
print("\n--- Scenario 2: File Not Found Error ---")
process_data("missing_file.txt")