class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for i, c in enumerate(s):
            if hashmap[c] == 1:
                return i
        return -1