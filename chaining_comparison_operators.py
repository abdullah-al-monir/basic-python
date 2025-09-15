# -------------------------------
# Chaining Comparison Operators
# -------------------------------

print("Example 1: Check if age is between 18 and 30")

age = 25

if 18 <= age <= 30:
    print("Age is between 18 and 30")
else:
    print("Age is outside the range")
print()

# -------------------------------------

print("Example 2: Check if number is outside a range")

number = 45

if number < 0 or number > 100:
    print("Number is outside 0–100")
else:
    print("Number is within 0–100")
print()

# -------------------------------------

print("Example 3: Using chained comparisons with equality")

score = 100

if 0 <= score <= 100:
    print("Valid score")
else:
    print("Invalid score")
print()

# -------------------------------------

print("Example 4: Check temperature range")

temperature = 22

if 15 <= temperature <= 25:
    print("Comfortable temperature")
else:
    print("Too hot or too cold")
print()

# -------------------------------------

print("Example 5: Chaining with more than two comparisons")

x = 10

if 5 < x < 15 < 20:
    print("x is between 5 and 15, and 15 is less than 20")
else:
    print("Condition not met")
print()
