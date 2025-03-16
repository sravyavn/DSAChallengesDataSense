#Day2Question2: Filter strings based on criteria
strings=["apple","hi","python","art","sony","education"]
vowels=["a","e","i","o","u"]
def filter_strings(a,k,m):
    output=[]
    for i in range(len(a)):
        count=0
        word_length=len(a[i])
        for j in a[i]:
            if j in vowels:
                count+=1
        if count>=m and word_length>=k:
            output.append(a[i])
    return output
print(filter_strings(strings,4,2))