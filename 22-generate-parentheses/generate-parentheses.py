class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(Copen,Cclosed):
            if Copen == Cclosed == n:
                res.append(''.join(stack))
            
            if Copen < n:
                stack.append('(')
                backtrack(Copen+1,Cclosed)
                stack.pop()

            if Cclosed < Copen:
                stack.append(')')
                backtrack(Copen,Cclosed+1)
                stack.pop()
        
        backtrack(0,0)
        return res
            


        