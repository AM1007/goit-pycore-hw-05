from functools import reduce
import re
from typing import Callable

# Creation of a function - a number generator with text.
# The map function converts numbers into numbers based on the object used for filtering
# The filter function uses a one-time lambda function, which looks for numbers using a regular expression.
# The yield function allows you to rotate the previously found number to a new function call

def generator_numbers(text: str):
    numbers = map(float, filter(lambda x: re.match(r"\d+\.{0,1}\d+.",x), text.split(" ")))
    for number in numbers:
        yield number

# Calculation of the total amount of generated elements using the additional reduce function
def sum_profit(text: str, func: Callable):
    return reduce(lambda x, y: x + y, func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")