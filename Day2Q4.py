#Day2Q4: Find 1st & last position of ele in sorted array
nums=[5,7,7,8,8,10]
target=8
first=[]
last=[]
if len(nums)==0 or target not in nums:
        places=[-1,-1]
        print(places)
else:
    def firstposition(nums,target):
        i=0
        for i in range(len(nums)):
            if nums[i]==target:
                first.append(i)
                print(f"First position is {first}")
                break
        return first
    def lastposition(nums,target):
        i=len(nums)-1
        while nums[i]!=target:
            i-=1
        else:
            last.append(i)
            print(f"Last position is {last}")
        return last
    firstposition(nums,target)
    lastposition(nums,target)




# nums=[5,7,7,8,8,10]
# target=8
# places=[]
# if len(nums)==0 or target not in nums:
#     places=[-1,-1]
# for i in range(len(nums)):
#     if nums[i]==target:
#         places.append(i)
# print(places)
