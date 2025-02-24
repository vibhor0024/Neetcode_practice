class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        RTL = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in RTL:
                if stack and stack[-1] == RTL[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False






        