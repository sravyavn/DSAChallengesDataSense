#Day6Q11:
s="eceba"
def longest_substring(s: str) -> int:
    l = 0  
    char_count = {}  
    max_len = 0  
    for r in range(len(s)):  
        char_count[s[r]] = char_count.get(s[r], 0) + 1  
        while len(char_count) > 2:
            char_count[s[l]] -= 1  
            if char_count[s[l]] == 0:
                del char_count[s[l]]  
            l += 1  
        max_len = max(max_len, r - l + 1)
    return max_len
print(longest_substring(s))