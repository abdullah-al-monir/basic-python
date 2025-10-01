# Special Sequences (\d, \w, \s, etc.) are shorthands for common character classes.
# Sets ([...]) define a custom set of characters to match.

import re

# String to test sequences and sets
TEST_STRING = "User: Jane_Doe ID: 456 Contact: (555) 123-4567"

# --- Special Sequences (Shorthands) ---

# 1. \d: Matches any digit (0-9). Equivalent to [0-9].
digits = re.findall(r'\d', TEST_STRING)
print(f"1. \d (Digits): {digits}") 

# 2. \D: Matches any non-digit character. Equivalent to [^0-9].
non_digits = re.findall(r'\D', "123abc456")
print(f"2. \D (Non-Digits, first 5): {non_digits[:5]}") 

# 3. \w: Matches any word character (a-z, A-Z, 0-9, _). Equivalent to [a-zA-Z0-9_].
words = re.findall(r'\w+', TEST_STRING)
print(f"3. \w+ (Words/IDs): {words}") 

# 4. \s: Matches any whitespace character (space, tab, newline).
spaces = re.findall(r'\s', TEST_STRING)
print(f"4. \s (Spaces): {len(spaces)} spaces found.")

# 5. \b and \B (Word Boundary): \b matches the start or end of a word. \B is the opposite.
match_b = re.search(r'\bID\b', TEST_STRING)
match_B = re.search(r'\Bane\B', TEST_STRING) # 'ane' not at a word boundary
print(f"\n5. \b (Boundary): Found 'ID': {bool(match_b)}")
print(f"   \B (Non-Boundary): Found 'ane' inside 'Jane': {bool(match_B)}")

# --- Sets (Character Classes) ---

# 6. Matching any character from a specific set.
# Matches 'a', 'b', 'c', or 'd'
set_match = re.findall(r'[abcd]', "bad cafe")
print(f"\n6. Set [abcd]: {set_match}") # ['b', 'a', 'd', 'a', 'c']

# 7. Negation within a set (^ inside brackets).
# Matches any character EXCEPT 'a', 'c', or 'd'.
neg_set_match = re.findall(r'[^acd]', "bad cafe")
print(f"7. Negation [^acd]: {neg_set_match}") # ['b', ' ', 'f', 'e']