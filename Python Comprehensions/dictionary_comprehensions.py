# Dictionary comprehensions create new dictionaries from an iterable.
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Example 1: Creating a dictionary where keys are items and values are their lengths.
words = ["sun", "moon", "star", "planet"]
word_lengths = {word: len(word) for word in words}
print(f"1. Dictionary of Word Lengths: {word_lengths}")
# Output: {'sun': 3, 'moon': 4, 'star': 4, 'planet': 6}

# Example 2: Filtering an existing dictionary to include only items with a score > 70.
scores = {'math': 85, 'history': 68, 'science': 92, 'art': 75}
high_scores = {subject: score for subject, score in scores.items() if score > 70}
print(f"2. Filtered Dictionary (High Scores): {high_scores}")
# Output: {'math': 85, 'science': 92, 'art': 75}

# Example 3: Mapping employee IDs to names using zip().
ids = [101, 102, 103]
employees = ["Anna", "Ben", "Cara"]
employee_map = {id_num: name for id_num, name in zip(ids, employees)}
print(f"3. Dictionary from Zipped Lists: {employee_map}")
# Output: {101: 'Anna', 102: 'Ben', 103: 'Cara'}