def increment(number, by=10):
    return number + by


print(increment(2, by=3))  # keyword
print(increment(5))  # empty parameter but has default value


#  xargs

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
