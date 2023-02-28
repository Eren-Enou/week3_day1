"""You must implement a function that returns the difference between the biggest and the smallest value in a list(lst) received as parameter.

The list(lst) contains integers, which means it may contain some negative numbers.

If the list is empty or contains a single element, return 0.

The list(lst) is not sorted.

max_diff([1, 2, 3, 4]) # return 3, because 4 - 1 == 3
max_diff([1, 2, 3, -4]) # return 7, because 3 - (-4) == 7
"""

def max_diff(list):
    return max(list) - min(list)

print(max_diff([1,2,3,4]))
print(max_diff([1,2,3,-4]))