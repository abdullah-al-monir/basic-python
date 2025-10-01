set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2}

# 1. Union: Elements in either set A OR set B (removes duplicates)
union_result_func = set_a.union(set_b)
union_result_op = set_a | set_b
print(f"1. Union (A | B): {union_result_op}")

# 2. Intersection: Elements common to BOTH set A AND set B
intersection_result_func = set_a.intersection(set_b)
intersection_result_op = set_a & set_b
print(f"2. Intersection (A & B): {intersection_result_op}")

# 3. Difference: Elements in set A but NOT in set B
difference_result_func = set_a.difference(set_b)
difference_result_op = set_a - set_b
print(f"3. Difference (A - B): {difference_result_op}")
# Note the order matters:
print(f"   Difference (B - A): {set_b - set_a}")

# 4. Symmetric Difference: Elements in A OR B, but NOT in both (exclusive OR)
sym_diff_result_op = set_a ^ set_b
print(f"4. Symmetric Difference (A ^ B): {sym_diff_result_op}")

# 5. Subset Check (A <= B)
# Is set C a subset of set A? (Are all elements of C in A?)
is_subset = set_c.issubset(set_a)
print(f"5. Is C a subset of A? ({set_c} <= {set_a}): {is_subset}")

# 6. Superset Check (A >= B)
# Is set A a superset of set C? (Does A contain all elements of C?)
is_superset = set_a.issuperset(set_c)
print(f"6. Is A a superset of C? ({set_a} >= {set_c}): {is_superset}")