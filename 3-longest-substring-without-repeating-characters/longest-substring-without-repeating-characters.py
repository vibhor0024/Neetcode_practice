class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        set1 =  set()
        maximum = 0
        for r in range(len(s)):
            while s[r] in  set1:
                set1.remove(s[l])
                l += 1
            
            set1.add(s[r])
            maximum = max(maximum,r-l+1)
        
        return maximum

            
        