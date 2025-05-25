import math
#Python has a set of built-in math functions, including an extensive math module, 
# that allows you to perform mathematical tasks on numbers.
x = min(5, 10, 25)
y = max(5, 10, 25)
print('min()', x)
print('max()', y)

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print('abs()', x)

# The pow(x, y) function returns the value of x to the power of y (xy).
p = pow(3,4)
print('PoW()', p)

# The math.sqrt() method for example, returns the square root of a number:
s = math.sqrt(64)
print('Sqrt()',s)

# The math.ceil() method rounds a number upwards to its nearest integer, and 
# the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
c = math.ceil(1.4)
f = math.floor(1.4)
print('Floor()', f)
print('Ceil()', c)

# The math.pi constant, returns the value of PI (3.14...):
pi = math.pi
print('pi =',pi)