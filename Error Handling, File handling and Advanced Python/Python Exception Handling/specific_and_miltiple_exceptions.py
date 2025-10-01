# Demonstrates how to catch different exceptions for precise handling.

data_record = ['Product-X', 5, '30.50'] # A list: [name, quantity, price_str]

def calculate_inventory_value(record):
    """Calculates total value, handling various data issues."""
    try:
        product_name = record[0]
        quantity = int(record[1])      # Possible ValueError or IndexError
        price = float(record[2])       # Possible ValueError or IndexError
        
        total_value = quantity * price
        print(f"Product: {product_name}, Total Value: ${total_value:.2f}")

    # 1. Catching specific exceptions separately for different messages
    except ValueError:
        print("Data Error: Quantity or price could not be converted to a number.")
        
    # 2. Catching multiple exceptions in one block (TypeError and IndexError)
    except (TypeError, IndexError) as e:
        # TypeError might occur if record[1] was None, IndexError if record is too short
        print(f"Data Structure Error: Missing fields or incorrect data type usage. Detail: {e}")

    # 3. Catch-all handler (use with caution, as it hides error details)
    except Exception as e:
        print(f"Unforeseen Error: An unexpected issue occurred. Detail: {e}")


print("--- Test 1: Successful Calculation ---")
calculate_inventory_value(data_record)

print("\n--- Test 2: Triggering ValueError (Invalid price string) ---")
calculate_inventory_value(['Product-Y', 10, 'high'])

print("\n--- Test 3: Triggering IndexError (Missing price field) ---")
calculate_inventory_value(['Product-Z', 5])