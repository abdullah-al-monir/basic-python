# --------------------------------------
# Logical Operators in Python: and, or, not
# --------------------------------------

# Example 1: 'and' operator
print("Example 1: 'and' operator")
rich = True
driving_license = False

if rich and driving_license:
    print("Buy a car.")
else:
    print("Can't buy a car.")
print()

# Example 2: 'or' operator
print("Example 2: 'or' operator")
has_passport = False
has_national_id = True

if has_passport or has_national_id:
    print("Can travel internationally.")
else:
    print("Cannot travel internationally.")
print()

# Example 3: 'not' operator
print("Example 3: 'not' operator")
student = True

if not student:
    print("Can't apply.")
else:
    print("Can apply.")
print()

# Example 4: 'and' with multiple conditions
print("Example 4: 'and' with multiple conditions")
age = 20
is_employed = True

if age >= 18 and is_employed:
    print("Eligible for a loan.")
else:
    print("Not eligible for a loan.")
print()

# Example 5: 'not' with a boolean
print("Example 5: 'not' with a boolean")
is_logged_in = False

if not is_logged_in:
    print("Please log in.")
else:
    print("Welcome back!")
print()

# Example 6: Combining 'and', 'or', 'not'
print("Example 6: Combining 'and', 'or', 'not'")
has_ticket = False
is_vip = True
is_guest_list = False

if has_ticket or (is_vip and not is_guest_list):
    print("Entry allowed.")
else:
    print("Entry denied.")
print()

# Example 7: Game decision logic
print("Example 7: Game logic with 'and' and 'not'")
has_sword = True
has_shield = False
enemy_nearby = True

if has_sword and enemy_nearby:
    print("Fight the enemy!")
elif not has_sword and enemy_nearby:
    print("Run away!")
else:
    print("You're safe.")
print()

# Example 8: Checking user access
print("Example 8: Access control with 'or' and 'not'")
is_admin = False
is_editor = True
is_banned = False

if (is_admin or is_editor) and not is_banned:
    print("Access granted.")
else:
    print("Access denied.")
print()
