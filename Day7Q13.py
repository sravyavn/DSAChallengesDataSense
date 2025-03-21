nums=[3,6,9,1]
nums1=[5]
def max_difference(nums):
    max_diff=[]
    l=0
    r=1
    nums=sorted(nums)
    if len(nums)<2:
        print(f" it is 0")
    else:
        while r<len(nums):
            max_diff.append(nums[r]-nums[l])
            l+=1
            r+=1
        print(f"The differences are {max_diff}")
        print(f"The max difference is {max(max_diff)}")
max_difference(nums)
