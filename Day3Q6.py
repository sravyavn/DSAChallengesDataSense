#Day3Q6: find len of longest substring without repeating chars
s="pwwkew"
def long_substring(s):
    set1 = set()
    l = 0
    longest = 0
    beginpoint = 0  

    for r in range(len(s)):
        while s[r] in set1:
            set1.remove(s[l])
            l += 1
        set1.add(s[r])
        if r - l + 1 > longest:
            longest = r - l + 1
            beginpoint = l

    substring = s[beginpoint:beginpoint + longest]
    print(f"The answer is \"{substring}\" with length of {longest}")

long_substring(s) 