#Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
def combinationSum3(k, n):
    result = []

    def backtrack(start, path, total):
        if len(path) == k and total == n:
            result.append(path[:])
            return
        if len(path) > k or total > n:
            return
        
        for i in range(start, 10):  # numbers 1 through 9
            path.append(i)
            backtrack(i + 1, path, total + i)
            path.pop()  # backtrack

    backtrack(1, [], 0)
    return result

print(combinationSum3(3, 7)) 
print(combinationSum3(3, 9))   
print(combinationSum3(4, 1)) 