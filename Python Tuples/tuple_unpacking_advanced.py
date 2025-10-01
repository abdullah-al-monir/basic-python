# Unpacking with the asterisk (*) operator to grab multiple items into a list.


# Example 1: Capturing middle elements
data_tuple = ('Jan', 31, 2024, 'Cloudy', 0.5)

# 'month' gets the first item ('Jan')
# 'day' gets the second item (31)
# '*rest' collects everything in between (2024, 'Cloudy') into a list
# 'rainfall' gets the last item (0.5)
month, day, *rest, rainfall = data_tuple

print(f"1. Original Tuple: {data_tuple}")
print(f"   Month: {month}")
print(f"   Day: {day}")
print(f"   Rest (collected as a list): {rest}")
print(f"   Rainfall: {rainfall}")

print("-" * 20)

# Example 2: Capturing elements at the end
# 'start' gets the first item
# '*middle_items' collects everything up to the last two elements
# 'end_1' gets the second to last item
# 'end_2' gets the last item
long_tuple = (100, 101, 102, 103, 104, 105, 106)
start, *middle_items, end_1, end_2 = long_tuple

print(f"2. Original Tuple: {long_tuple}")
print(f"   Start: {start}")
print(f"   Middle Items: {middle_items}")
print(f"   End 1: {end_1}")
print(f"   End 2: {end_2}")