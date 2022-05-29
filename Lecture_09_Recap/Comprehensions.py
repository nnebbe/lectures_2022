import numpy as np

a = [np.nan, 5, "hello", 42]
b = np.arange(1, 100)

filtered_nans = [x for x in a if (True if isinstance(x, str) else not np.isnan(x))]
# Alternatively use that np.nan == np.nan will return false
# filtered_nans = [x for x in a if x == x]

filtered_division = [x for x in b if not x%7 and x%2]

appended_hello = [str(x)+" says hello" for x in a]

is_dividable = {str(x)+" is dividable": not x%7 and bool(x%2) for x in b}