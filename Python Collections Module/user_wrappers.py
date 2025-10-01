from collections import UserDict, UserList, UserString

# UserDict, UserList, and UserString are base classes for creating custom containers
# that inherit most behavior from built-in types while allowing modification/extension.

# 1. Custom Dictionary (UserDict) - Example: Read-Only Keys


class ImmutableKeyDict(UserDict):
    # Overrides __setitem__ to prevent adding/changing certain keys
    def __setitem__(self, key, value):
        if key in self.data and key in ['admin', 'root']:
            raise PermissionError(f"Key '{key}' is read-only.")
        super().__setitem__(key, value)


secure_config = ImmutableKeyDict({'admin': 1, 'user': 100})
print("1. Custom Dict (ImmutableKeyDict):")
try:
    secure_config['user'] = 101  # Allowed
    secure_config['admin'] = 2  # Disallowed
except PermissionError as e:
    print(f"   Error encountered: {e}")
print(f"   Final data: {secure_config}")


# 2. Custom List (UserList) - Example: Force Uppercase on Insert
class UppercaseList(UserList):
    # Overrides append to force string elements to uppercase
    def append(self, item):
        if isinstance(item, str):
            item = item.upper()
        super().append(item)


my_items = UppercaseList(["alpha", "beta"])
my_items.append("gamma")
my_items.append(123)
print("\n2. Custom List (UppercaseList):")
print(f"   List after insertion: {my_items}")


# 3. Custom String (UserString) - Example: Simple string modification methods
class ReversibleString(UserString):
    # Adds a new method to the string object
    def reverse(self):
        return self.data[::-1]

    # Overrides the capitalize method
    def capitalize(self):
        return self.data.upper()  # Modified functionality


s = ReversibleString("test_string")
print("\n3. Custom String (ReversibleString):")
print(f"   Original: {s}")
print(f"   Reversed (new method): {s.reverse()}")
print(f"   Capitalized (modified method): {s.capitalize()}")
