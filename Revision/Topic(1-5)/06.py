# Question 6

# Without using any built-in sorting function, arrange the following list in ascending order.

# numbers = [8, 3, 10, 1, 6, 5]

# The interviewer is more interested in your logic than the algorithm's efficiency.
from functools import cache
@cache
def square(n):
    return n*n
print(square(5))