#Day17Q33:
weights = [3,2,2,4,1,4]
days = 3
def shipWithinDays(weights, days):
    def can_ship(capacity):
        curr = 0
        needed_days = 1  
        for w in weights:
            if curr + w > capacity:
                needed_days += 1
                curr = 0
            curr += w
        return needed_days <= days

    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    #print(left)
    return left
    
print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))      # Output: 15
print(shipWithinDays([3,2,2,4,1,4], 3))               # Output: 6
print(shipWithinDays([1,2,3,1,1], 4))                 # Output: 3