# Set comprehensions create a set, automatically ensuring unique elements.
# Syntax: {expression for item in iterable if condition}

# Example 1: Extracting unique characters from a string.
text = "programming language is fun"
unique_chars = {char for char in text if char != ' '}
print(f"1. Set of Unique Characters: {unique_chars}")
# Output (Order may vary): {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n', 'l', 'u', 'e', 's', 'f'}

# Example 2: Creating a set of multiples of 5, ensuring no duplicates.
numbers = [5, 10, 15, 20, 10, 25, 5, 30]
multiples_of_five = {num for num in numbers if num % 5 == 0}
print(f"2. Set of Unique Multiples of 5: {multiples_of_five}")
# Output (Order may vary): {25, 10, 5, 30, 20, 15}

# Example 3: Finding the unique result of an operation on a range.
# Calculates the remainder when dividing by 3.
remainders = {i % 3 for i in range(10)}
print(f"3. Set of Unique Remainders (i % 3): {remainders}")
# Output: {0, 1, 2}