#Day7Q13: in an array, find the no.of triplets that can form a triangle
from itertools import combinations

nums=[2,2,3,4]
nums2=[4,2,3,4]
triplets=[]
def find_triplets(nums):
    
    for a,b,c in combinations(nums,3):
        if a+b>c and b+c>a and c+a>b:
            triplets.append([a,b,c])
    print(len(triplets))
find_triplets(nums2)