import math

print(round(5.6))  # Rounds 5.6 to the nearest integer (Output: 6)
print(abs(-6.7))   # Returns the absolute (positive) value of -6.7 (Output: 6.7)
# Returns the smallest integer greater than or equal to 2.2 (Output: 3)
print(math.ceil(2.2))

# Additional math module methods with examples
# Trigonometric functions (angles in radians)
print(math.sin(math.pi / 2))  # Sine of 90 degrees (π/2 radians) (Output: 1.0)
print(math.cos(0))            # Cosine of 0 radians (Output: 1.0)
# Tangent of 45 degrees (π/4 radians) (Output: ~1.0)
print(math.tan(math.pi / 4))
# Arcsine (inverse sine) of 1, returns angle in radians (Output: ~1.5708)
print(math.asin(1))
print(math.acos(0))           # Arccosine (inverse cosine) of 0 (Output: ~1.5708)
# Arctangent (inverse tangent) of 1 (Output: ~0.7854)
print(math.atan(1))

# Hyperbolic functions
print(math.sinh(1))  # Hyperbolic sine of 1 (Output: ~1.1752)
print(math.cosh(1))  # Hyperbolic cosine of 1 (Output: ~1.5431)
print(math.tanh(1))  # Hyperbolic tangent of 1 (Output: ~0.7616)

# Power and logarithmic functions
print(math.pow(2, 3))     # 2 raised to the power of 3 (Output: 8.0)
print(math.sqrt(16))      # Square root of 16 (Output: 4.0)
print(math.log(2.7183))   # Natural logarithm (base e) of ~e (Output: ~1.0)
print(math.log10(100))    # Base-10 logarithm of 100 (Output: 2.0)
print(math.log2(8))       # Base-2 logarithm of 8 (Output: 3.0)
print(math.exp(1))        # e raised to the power of 1 (Output: ~2.7183)

# Rounding and absolute value functions
print(math.floor(2.7))    # Largest integer less than or equal to 2.7 (Output: 2)
print(math.trunc(2.7))    # Truncates decimal part of 2.7 (Output: 2)
print(math.fabs(-5.2))    # Absolute value of -5.2 (Output: 5.2)

# Constants in math module
print(math.pi)            # Mathematical constant π (Output: ~3.1416)
print(math.e)             # Mathematical constant e (Output: ~2.7183)
print(math.tau)           # Mathematical constant τ (2π) (Output: ~6.2832)
print(math.inf)           # Positive infinity (Output: inf)
print(math.nan)           # Not a Number (NaN) (Output: nan)

# Angular conversion functions
print(math.degrees(math.pi))  # Converts π radians to degrees (Output: 180.0)
# Converts 180 degrees to radians (Output: ~3.1416)
print(math.radians(180))

# Combinatorial functions
# Factorial of 5 (5! = 5 * 4 * 3 * 2 * 1) (Output: 120)
print(math.factorial(5))
# Number of ways to choose 2 items from 5 (Output: 10)
print(math.comb(5, 2))
# Number of ways to arrange 2 items from 5 (Output: 20)
print(math.perm(5, 2))

# Other useful functions
# Checks if 10 is finite (not inf or nan) (Output: True)
print(math.isfinite(10))
print(math.isinf(math.inf))   # Checks if value is infinite (Output: True)
print(math.isnan(math.nan))   # Checks if value is NaN (Output: True)
print(math.gcd(48, 18))      # Greatest common divisor of 48 and 18 (Output: 6)
print(math.lcm(12, 18))      # Least common multiple of 12 and 18 (Output: 36)
print(math.fmod(10.5, 3))    # Modulus for floating-point numbers (Output: 1.5)
print(math.erf(1))           # Error function at 1 (Output: ~0.8427)
# Gamma function at 5 (equivalent to (5-1)!) (Output: 24.0)
print(math.gamma(5))
