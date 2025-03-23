# nums = [2,3,1,1,4]
# def jumpgame(nums):
#     i=1
#     while i<len(nums):
#         x = nums[i]
#         i=i+x
#     print(f"final position is {x}")
#     if i==len(nums)-1:
#         print("true")
#     else:
#         print("false")
# jumpgame(nums)

nums = [2,3,1,1,4]
nums1 = [3,2,1,0,4]
def canJump(nums):
        max_reach = 0  
        
        for i, num in enumerate(nums):
            if i > max_reach:
                return False  
            
            max_reach = max(max_reach, i + num)  
            
            if max_reach >= len(nums) - 1:
                return True 
        
        return False
print(canJump(nums))