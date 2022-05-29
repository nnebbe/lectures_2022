import numpy as np

# For a more elegant solution, have a look at the respective comprehension
filter_nans = lambda x: True if isinstance(x, str) else not np.isnan(x)

filter_division = lambda  x: not x%7 and x%2

append_hello = lambda x: str(x)+" says hello"

find_value = lambda x, y: x if x/7%6 <= y/7%6 else y
