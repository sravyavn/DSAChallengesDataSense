#Day12Q24: Maximum consecutive ones
nums=[1,0,1,1,0,1]
def max_consecutive_ones(nums):
    l = 0  # Left pointer
    max_len = 0
    flip = 0  # Counts flipped zeros

    for r in range(len(nums)):
        if nums[r] == 0:
            flip += 1
        
        while flip > 1:  # More than one zero flipped, move `l`
            if nums[l] == 0:
                flip -= 1
            l += 1
        
        max_len = max(max_len, r - l + 1)
    print(max_len)
    return max_len

max_consecutive_ones(nums)