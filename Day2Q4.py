#Day2Q4: Find 1st & last position of ele in sorted array
nums=[5,7,7,8,8,10]
target=8
places=[]
if len(nums)==0 or target not in nums:
    places=[-1,-1]
for i in range(len(nums)):
    if nums[i]==target:
        places.append(i)
print(places)