# Defining custom exceptions allows for application-specific, clear error types.

# Custom exceptions should inherit from the base 'Exception' class.
class InventoryError(Exception):
    """Base class for exceptions in this inventory management system."""
    pass

class NegativeQuantityError(InventoryError):
    """Raised when an attempt is made to set a negative product quantity."""
    def __init__(self, quantity):
        self.message = f"Product quantity cannot be negative. Received: {quantity}"
        super().__init__(self.message)

class ProductNotFoundError(InventoryError):
    """Raised when a specified product ID does not exist."""
    pass

def update_stock(product_id, quantity):
    """Simulates updating product stock, using custom exceptions for validation."""
    
    # Validation 1: Check for invalid quantity
    if quantity < 0:
        raise NegativeQuantityError(quantity)
        
    # Validation 2: Simulate check for existing product
    if product_id == 999:
        raise ProductNotFoundError(f"Product ID {product_id} not found in database.")
        
    print(f"Stock updated successfully for Product {product_id}. New quantity: {quantity}")

# --- Test Cases ---

# Test 1: Valid update
try:
    update_stock(105, 50)
except InventoryError as e:
    print(f"Handled Custom Error: {e}")

print("\n" + "="*20 + "\n")

# Test 2: Trigger NegativeQuantityError
try:
    update_stock(105, -10)
except NegativeQuantityError as e:
    print(f"Handled Custom Error: {e}")

print("\n" + "="*20 + "\n")

# Test 3: Trigger ProductNotFoundError
try:
    update_stock(999, 5)
except ProductNotFoundError as e:
    print(f"Handled Custom Error: {e}")