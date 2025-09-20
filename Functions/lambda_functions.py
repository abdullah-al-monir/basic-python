# Lambda Functions are anonymous functions means that the function is without a name. As we already know def keyword is used to define a normal function in Python. Similarly, lambda keyword is used to define an anonymous function in Python. Lambda functions are also called as “Inline functions” because they are defined in a single line.

# Syntax
# lambda arguments : expression
# lambda: The keyword to define the function.
# arguments: A comma-separated list of input parameters (like in a regular function).
# expression: A single expression that is evaluated and returned.

s1 = 'PythonWorld'
def s2(func): return func.upper()


print(s2(s1))


# 1. Using with condition checking
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"


print(n(5))
print(n(-3))
print(n(0))

# 2. Using with List Comprehension

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
    
# 3. Using for Returning Multiple Results
calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

# 4. Using with filter()
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

# 5. Using with map()
n = [1, 2, 3, 4, 5, 6]
square = map(lambda x: x * x, n)
print(list(square))

# 6. Using with reduce()
from functools import reduce
n = [1, 2, 3, 4, 5, 6]
sum = reduce(lambda x, y: x + y, n)
print(sum)



# Feature	            lambda Function	                             Regular Function (def)
# Definition       Single expression with lambda.	                 Multiple lines of code.
# Name	          Anonymous (or named if assigned).                 	Must have a name.
# Statements         Single expression only.	                     Can include multiple statements.
# Documentation	  Cannot have a docstring.	                     Can include docstrings.
# Reusability    Best for short, temporary functions.     	     Better for reusable and complex logic.