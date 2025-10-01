# Demonstrates how to manually raise a built-in exception to enforce logic or validation.

def set_security_level(level):
    """Validates and sets a security level, raising ValueError if invalid."""
    valid_levels = ['low', 'medium', 'high']
    
    if level.lower() not in valid_levels:
        # Raise a built-in exception with a clear, descriptive message
        raise ValueError(f"Invalid security level: '{level}'. Must be one of {valid_levels}")
        
    print(f"Security level set to: {level.upper()}")

# Scenario 1: Valid input
try:
    set_security_level("medium")
except ValueError as e:
    print(f"Caught Error: {e}")

print("\n" + "="*20 + "\n")

# Scenario 2: Invalid input (Triggers the raise statement)
try:
    set_security_level("critical")
except ValueError as e:
    # The calling code catches the exception we raised
    print(f"Caught Error: {e}")
    
print("\nProgram continues after handling the raised exception.")