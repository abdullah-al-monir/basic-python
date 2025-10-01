my_tuple = ('A', 'B', 'C', 'D', 'E', 'F')

# 1. Accessing elements using positive indexing
print(f"1. Element at index 0 (first): {my_tuple[0]}")
print(f"   Element at index 3: {my_tuple[3]}")

# 2. Accessing elements using negative indexing
print(f"2. Element at index -1 (last): {my_tuple[-1]}")
print(f"   Element at index -3: {my_tuple[-3]}")

# 3. Accessing a range of elements using slicing [start:stop]
# Elements from index 1 up to (but not including) index 4
slice_1_4 = my_tuple[1:4]
print(f"3. Slice [1:4]: {slice_1_4}") 

# 4. Slicing from the beginning up to an index [:stop]
slice_to_3 = my_tuple[:3]
print(f"4. Slice [:3]: {slice_to_3}")

# 5. Slicing from an index to the end [start:]
slice_from_4 = my_tuple[4:]
print(f"5. Slice [4:]: {slice_from_4}")

# 6. Tuple Unpacking
coordinates = (10.5, 20.2, 5.0)
x, y, z = coordinates
print(f"6. Unpacked X coordinate: {x}")
print(f"   Unpacked Y coordinate: {y}")
print(f"   Unpacked Z coordinate: {z}")