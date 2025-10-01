# Demonstrates the creation and consumption of iterators using built-in types.

# 1. Iterable: A tuple of monthly sales figures.
monthly_sales = (1500, 2200, 1800, 3100)
print(f"Original Iterable (Tuple): {monthly_sales}")

# 2. Creating an Iterator: The iter() function calls the object's __iter__() method.
sales_iterator = iter(monthly_sales)
print(f"Created Iterator Object: {sales_iterator}")

# 3. Consuming the Iterator: The next() function calls the iterator's __next__() method.
print("\nConsuming items one by one:")
print(f"  First month: {next(sales_iterator)}")
print(f"  Second month: {next(sales_iterator)}")

# 4. Iterators maintain state: A for loop can continue where next() left off.
print("\nConsuming the rest with a for loop:")
for sale in sales_iterator:
    print(f"  Remaining month: {sale}")

# Note: Once exhausted, the iterator is finished and cannot restart.