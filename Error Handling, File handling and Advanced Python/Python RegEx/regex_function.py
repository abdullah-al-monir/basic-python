import re

TEXT = "The code version is v1.2.3 and the fix version is v1.3.0."
VERSION_PATTERN = r'v(\d+\.\d+\.\d+)' # Matches version strings like v1.2.3

# 1. re.search(): Finds the first occurrence of the pattern. Returns a Match Object or None.
first_match = re.search(VERSION_PATTERN, TEXT)
if first_match:
    print(f"1. re.search() (First Match): {first_match.group(0)}")
    # group(1) contains the content captured inside the parentheses
    print(f"   Extracted version: {first_match.group(1)}")

# 2. re.findall(): Finds all non-overlapping matches and returns them as a list.
all_matches = re.findall(VERSION_PATTERN, TEXT)
print(f"\n2. re.findall() (All captured groups): {all_matches}")
# Note: If groups are defined (parentheses), findall returns the captured groups, not the full match.

# 3. re.sub(): Replaces occurrences of the pattern with a replacement string.
replaced_text = re.sub(VERSION_PATTERN, '[REDACTED]', TEXT)
print(f"\n3. re.sub() (Replacement): {replaced_text}")

# 4. re.subn(): Replaces and returns a tuple (new_string, count_of_substitutions).
result_tuple = re.subn(VERSION_PATTERN, 'vX.X.X', TEXT)
print(f"\n4. re.subn() (Replacement and Count): {result_tuple}")

# 5. re.split(): Splits the string by the pattern occurrences.
date_string = "2023-10-01/2023-10-31"
parts = re.split(r'[/-]', date_string)
print(f"\n5. re.split() (Splitting by '-' or '/'): {parts}")

# 6. re.compile(): Compiles a pattern for efficiency and reuse.
# Useful when the same pattern is used many times.
compiled_pattern = re.compile(r'\d{3}') # Matches 3 consecutive digits
numbers = compiled_pattern.findall("ID: 123, PIN: 456, Code: 789")
print(f"\n6. re.compile() (Reusable pattern): {numbers}")