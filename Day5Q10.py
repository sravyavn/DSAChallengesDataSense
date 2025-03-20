#Day5Q10: print largest number possible using integers in an array
from functools import cmp_to_key
nums=[3,34,30,5,9]

def largestNumber(nums):
    nums = list(map(str, nums))
    def compare(x, y):
        return (int(y + x) - int(x + y))  # Sort in descending order
    nums.sort(key=cmp_to_key(compare))
    result = "".join(nums)
    return "0" if result[0] == "0" else result

print(largestNumber(nums))