# -----------------------------------------------------------------------------
# Description: Shows how to access and modify dictionary items.
# -----------------------------------------------------------------------------

user_profile = {
    "username": "mr_colon_three",
    "email": "mrcolonthreee.com",
    "is_active": True
}

# Access a value using its key in square brackets.
print(f"Accessing username with []: {user_profile['username']}")

# Using the get() method to access a value.
# It returns None if the key doesn't exist, preventing a KeyError.
print(f"Accessing email with get(): {user_profile.get('email')}")
print(f"Accessing a non-existent key: {user_profile.get('age')}")

# Add a new key-value pair.
user_profile["age"] = 30
print(f"After adding 'age': {user_profile}")

# Update the value of an existing key.
user_profile["email"] = "pypro@example.com"
print(f"After updating 'email': {user_profile}")
