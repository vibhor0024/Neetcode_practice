class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window = {}
        Tcount = {}
        minimum = float("infinity")
        have = 0
        
        res = [-1,-1]
        l = 0

        for c in t:
            Tcount[c] = 1 + Tcount.get(c, 0)
        need = len(Tcount)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in Tcount and window[c] == Tcount[c]:
                have +=1
            
            while have == need:
                if r-l+1 < minimum:
                    res = [l,r]
                    minimum = r-l+1
                
                window[s[l]] -= 1
                if s[l] in Tcount and window[s[l]] < Tcount[s[l]]:
                    have -= 1
                
                l += 1
        l,r = res
        return s[l:r+1] if minimum != float("infinity") else ""