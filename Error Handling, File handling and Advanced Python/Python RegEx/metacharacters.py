import re

# Metacharacters give the pattern special meaning (not literal matching).

STRING_1 = "cat, coat, count, cot"
STRING_2 = "File_1.txt, File_2.pdf, File-3.log"

# 1. . (Dot): Matches any single character (except newline).
match_dot = re.findall(r'c.t', STRING_1) 
print(f"1. Dot (.): Matches c.t in '{STRING_1}': {match_dot}") # ['cat', 'cot']

# 2. * (Star): Matches zero or more occurrences of the preceding element.
match_star = re.findall(r'co*t', STRING_1) # Matches c, followed by zero or more o's, then t
print(f"\n2. Star (*): Matches co*t: {match_star}") # ['cot', 'coot', 'cot'] if 'coot' existed

# 3. + (Plus): Matches one or more occurrences of the preceding element.
match_plus = re.findall(r'co+t', STRING_1) 
print(f"3. Plus (+): Matches co+t: {match_plus}") # ['coat', 'cot'] if 'cot' was written with a single 'o'

# 4. ? (Question Mark): Matches zero or one occurrence of the preceding element (optional).
match_optional = re.findall(r'colou?r', "color, colour, colr") 
print(f"4. Question Mark (?): Matches colou?r: {match_optional}") # ['color', 'colour', 'colr']

# 5. [] (Character Class): Matches any single character inside the brackets.
# Matches any digit from 1 to 3 or the letter 'b'.
match_class = re.findall(r'[1-3b]', "a1b2c3d4e") 
print(f"5. Character Class []: Matches [1-3b]: {match_class}") # ['1', 'b', '2', '3']

# 6. ^ and $ (Start and End): Anchors the match to the beginning/end of the string.
match_start = re.search(r'^File', STRING_2)
match_end = re.search(r'log$', STRING_2)
print(f"\n6. Anchors (^,$): Starts with 'File': {bool(match_start)}")
print(f"   Ends with 'log': {bool(match_end)}") # False, because 'log' is followed by a newline/EOF

# 7. | (OR): Matches either the pattern on the left or the right.
match_or = re.findall(r'txt|pdf', STRING_2)
print(f"7. OR (|): Matches 'txt' or 'pdf': {match_or}") # ['txt', 'pdf']

# 8. () (Grouping): Groups patterns, allows repetition on the group, and extracts sub-matches.
match_group = re.search(r'(\w+)\.pdf', STRING_2)
print(f"8. Grouping (): Extract word before .pdf: {match_group.group(1) if match_group else None}") # File_2