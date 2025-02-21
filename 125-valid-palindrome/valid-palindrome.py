class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s)-1

        while (l<r):
            while l<r and not self.alphan(s[l]):
                l += 1
            while l<r and not self.alphan(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l +=1 
            r -= 1
        
        return True
            

    def alphan(self, x):
        if ord(x) >= 97 and ord(x) <= 122 or  \
           ord(x) >= 65 and ord(x) <= 90 or   \
           ord(x) >= 48 and ord(x) <= 57:
           return True
        
        else:
            return False
        