#Day3Q5: Prod of each list elements except itself
from functools import reduce

nums=[-1,1,0,-3,3]
list=[]
for i in nums:   #list wasn't refreshing so used temp as copy of nums and didn't disturb nums
    temp=nums[:]
    temp.remove(i)
    output=reduce(lambda x,y:x*y,temp)
    list.append(output)
print(list)