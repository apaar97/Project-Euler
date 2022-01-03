#   Factorial digit sum

import math

num = math.factorial(100)
print(sum(int(x) for x in str(num)))
