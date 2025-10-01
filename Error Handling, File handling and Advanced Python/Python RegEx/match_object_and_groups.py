# The Match Object is returned by re.search() or re.match() on success, 
# providing methods to extract match details.

import re

LOG_ENTRY = "Error [CODE: 404] Time: 2023-10-01"
# Pattern to extract CODE and Date
LOG_PATTERN = r'\[CODE: (\d+)\] Time: (\d{4}-\d{2}-\d{2})'

match = re.search(LOG_PATTERN, LOG_ENTRY)

if match:
    print("--- Match Object Details ---")
    
    # 1. Getting the original string and regex pattern
    print(f"1. Original String (match.string): {match.string}")
    print(f"   Regex Pattern (match.re): {match.re}")
    
    # 2. Getting index/span details
    print(f"\n2. Index/Span:")
    print(f"   Start Index (match.start()): {match.start()}")
    print(f"   End Index (match.end()): {match.end()}")
    print(f"   Span Tuple (match.span()): {match.span()}")
    
    # 3. Getting matched content
    print(f"\n3. Matched Content:")
    # group(0) returns the entire match
    print(f"   Full Match (group(0)): {match.group(0)}") 
    # group(1), group(2), etc. return captured groups (content inside parentheses)
    print(f"   Error Code (group(1)): {match.group(1)}")
    print(f"   Date (group(2)): {match.group(2)}")
    # groups() returns a tuple of all captured groups
    print(f"   All Groups (groups()): {match.groups()}")
    
    # 4. Named Groups
    # Define groups with names: (?P<name>...)
    NAME_PATTERN = r'(?P<first>\w+)\s+(?P<last>\w+)'
    name_match = re.search(NAME_PATTERN, "Agent Smith")
    
    if name_match:
        # Access group by name
        print(f"\n4. Named Group (Last Name): {name_match.group('last')}")
        # groupdict() returns a dictionary of named groups
        print(f"   Group Dict: {name_match.groupdict()}")
else:
    print("No match found.")