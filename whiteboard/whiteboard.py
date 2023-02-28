# Given a list of integers, write a function determining whether the sum of its elements is odd or even.

# Return your answer as a string matching "odd" or "even".

# If the input array is empty, consider it as [0](array with a zero).

def solution(list_nums):
    # write your code here
    total = 0
    for num in list_nums:
        total += num
    if total % 2 == 0:
        return "even"
    else:
        return "odd"
print(solution([0, 1, 4]))
