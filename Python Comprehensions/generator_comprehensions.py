# Generator comprehensions create an iterator (generator object) that yields values lazily.
# Syntax: (expression for item in iterable if condition)

# Example 1: Creating a generator for all odd numbers in a large range.
# Note: The generator is created instantly and uses very little memory.
large_range_odds = (num for num in range(1000) if num % 2 != 0)
print(f"1. Generator Object Created: {large_range_odds}")
print(f"   First 5 Odd Numbers: {[next(large_range_odds) for _ in range(5)]}")
# Output: [1, 3, 5, 7, 9]

# Example 2: Calculating powers of 2 using a generator.
powers_of_two_gen = (2 ** i for i in range(1, 6))

# Converting the generator to a tuple to access all values at once
result_tuple = tuple(powers_of_two_gen)
print(f"2. Generator converted to Tuple: {result_tuple}")
# Output: (2, 4, 8, 16, 32)

# Example 3: Using a generator expression directly inside a function (e.g., sum()).
data_points = [10, 12, 15, 8, 11]
# Sum of all data points greater than 10
total_sum = sum(p for p in data_points if p > 10)

print(f"3. Sum of elements > 10 (using generator in sum()): {total_sum}")
# Output: 12 + 15 + 11 = 38