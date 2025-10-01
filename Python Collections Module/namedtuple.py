from collections import namedtuple

# namedtuple creates easy-to-read, self-documenting tuple subclasses with named fields.

# 1. Declaring a namedtuple structure
# Creates a class named 'Point' with fields 'x' and 'y'
Point = namedtuple('Point', ['x', 'y']) 

# Creating an instance of the namedtuple
p1 = Point(x=10, y=20) 
p2 = Point(30, 40) # Values can be passed positionally

print(f"1. Point p1: {p1}")
print(f"   Type of p1: {type(p1)}")

# 2. Accessing elements by index (like a regular tuple)
print(f"2. X-coordinate by index: {p1[0]}") 

# 3. Accessing elements by name (improves readability)
print(f"3. Y-coordinate by name: {p2.y}") 

# 4. Conversion Operations
# _make(): Create a namedtuple instance from an iterable
coordinates_list = [5, 5]
p3 = Point._make(coordinates_list)
print(f"4. Created from iterable (_make): {p3}")

# _asdict(): Convert to an OrderedDict
p1_dict = p1._asdict()
print(f"   Converted to OrderedDict (_asdict): {p1_dict}")
print(f"   Type of converted object: {type(p1_dict)}")