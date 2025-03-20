#Day59: Peak element's index in an array
nums=[1,2,1,3,5,6,4]
max1 = nums[0]
for i in range(len(nums)):
    if nums[i]>=max1:
        max1=nums[i]
print(max1)
print(max(nums))
