# Generator Expressions offer a concise, memory-efficient way to create a generator.
# Syntax: (expression for item in iterable) - Uses parentheses () instead of list comprehensions' []

data = [10, 25, 50, 75, 100]

# 1. Generator Expression: Creates an iterator lazily
# Generates (value + 5) for items > 20
increment_gen = (item + 5 for item in data if item > 20)

print(f"1. Generator Expression created (Type: {type(increment_gen)})")

# 2. Consuming the generator - values are computed one at a time
print("\n2. Consuming values:")
print(f"  First value: {next(increment_gen)}") # Computes 25 + 5 = 30
print(f"  Second value: {next(increment_gen)}") # Computes 50 + 5 = 55

# 3. Consumption in a loop
print("\n3. Consuming remainder:")
for result in increment_gen:
    print(f"  Remaining value: {result}") 

# 4. Comparison to List Comprehension
# List comprehension computes ALL values upfront, consuming more memory.
increment_list = [item + 5 for item in data if item > 20] 
print(f"\n4. List Comprehension (Type: {type(increment_list)})")
# This list is fully stored in memory: [30, 55, 80, 105]