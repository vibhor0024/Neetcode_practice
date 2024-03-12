class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0, len(s) - 1
        while l<r:
            while l<r and not self.alphanumeric(s[l]):
                 l += 1
            while r>l and not self.alphanumeric(s[r]):
                 r -= 1  
            if s[l].lower() != s[r].lower():
                 return False
            l += 1
            r -= 1
        return True

    def alphanumeric(self,letter):
        return (65 <= ord(letter) <= 90) or \
        (97 <= ord(letter) <= 122) or \
        (48 <= ord(letter) <= 57) 


        

