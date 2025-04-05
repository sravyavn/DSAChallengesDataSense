#Day15Q29: find the longest continuous substring with same chars after replacing at most k characters.
from collections import Counter

def characterReplacement(s, k):
    left = 0
    max_freq = 0
    char_count = Counter()
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1
        max_freq = max(max_freq, char_count[s[right]])

        # when invalid window
        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

    
        max_length = max(max_length, right - left + 1)

    return max_length


print(characterReplacement("ABAB", 2))  
print(characterReplacement("AABABBA", 1))  