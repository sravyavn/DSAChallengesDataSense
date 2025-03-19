#Day4Q8: Min size subarray sum
nums=[2,3,1,2,4,3]
target=7
def subarr(nums,target):
    l = 0
    sum = 0
    min_length = float('inf')
    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            min_length = min(min_length, r - l + 1)
            sum -= nums[l]
            l += 1

    return min_length if min_length != float('inf') else 0
print(subarr(nums,target))