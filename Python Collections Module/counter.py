from collections import Counter 

# Counter is used to tally hashable objects. Keys are items, values are counts.

# 1. Creating Counter from a list (Sequence of items)
fruit_basket = ['apple', 'orange', 'apple', 'banana', 'orange', 'apple']
fruit_counts = Counter(fruit_basket)
print(f"1. Counter from List: {fruit_counts}")

# 2. Creating Counter from a dictionary (Pre-defined counts)
poll_results = {'Candidate_A': 150, 'Candidate_B': 210, 'Candidate_C': 90}
vote_counts = Counter(poll_results)
print(f"2. Counter from Dictionary: {vote_counts}")

# 3. Creating Counter using keyword arguments
score_counts = Counter(Win=5, Loss=3, Draw=2)
print(f"3. Counter from Keyword Arguments: {score_counts}")

# 4. Accessing elements and performing arithmetic
print(f"4. Count of 'apple': {fruit_counts['apple']}")
print(f"   Count of 'grape' (non-existent): {fruit_counts['grape']}") # Returns 0, not KeyError

# 5. Using .most_common()
top_two = fruit_counts.most_common(2)
print(f"5. Two most common fruits: {top_two}")