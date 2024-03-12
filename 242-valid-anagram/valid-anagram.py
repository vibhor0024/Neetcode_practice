class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sdict = {}
        tdict = {}

        for i in range(len(s)):
            sdict[s[i]] = 1 + sdict.get(s[i],0)
            tdict[t[i]] = 1 + tdict.get(t[i],0)

        for c in sdict:
            if sdict[c] != tdict.get(c,0):
                return False
        
        return True


        