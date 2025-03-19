#Day4Q7:Min diff between highest &lowest of k scores

nums=[9,4,1,7]
def min_diff(nums, k):
    if k == 1:
        return 0
    nums.sort()
    min_diff = float('inf')
    for i in range(len(nums) - k + 1):
        min_diff = min(min_diff, nums[i + k - 1] - nums[i])  
    return min_diff

print(min_diff(nums,2))