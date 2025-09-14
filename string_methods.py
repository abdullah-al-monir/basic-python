name = "Abdullah Al Monir"
# to make the whole string uppercase
print(name.upper())
# to make the whole string lowercase
print(name.lower());

# to find the index of specific part
print(name.find("Mo"))

# to replace 
print(name.replace("Mo","Fe"))

# is it in the string or not
print("Monir" in name)
print("Al" not in name)
company = "bug fix pros"

print(company.title());

left_space = "    Hey"
right_space = "Hey    "

# to remove whitespace
print(left_space.lstrip())
print(right_space.rstrip())