# Demonstrates the core try-except structure for basic error prevention.

def divide_numbers(numerator, denominator):
    """Attempts division and handles a ZeroDivisionError."""
    try:
        # Code that might raise an exception
        result = numerator / denominator
        print(f"Result of division: {result}")
        
    except ZeroDivisionError:
        # Code that executes if the specified exception occurs
        print("Error: Cannot perform division by zero.")
    
    except TypeError:
        # Handling another specific exception
        print("Error: Input types must be numbers.")


print("--- Test 1: Successful Division ---")
divide_numbers(100, 5)

print("\n--- Test 2: Handling ZeroDivisionError ---")
divide_numbers(100, 0)

print("\n--- Test 3: Handling TypeError ---")
divide_numbers(100, "hello")

print("\nProgram continues running after handling exceptions.")