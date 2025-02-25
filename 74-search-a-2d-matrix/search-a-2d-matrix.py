class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        L = 0
        R = m - 1

        l = 0
        r = n - 1

        while L <= R:
            MID = L + (R-L)//2

            if target < matrix[MID][0]:
                R = MID - 1
            
            elif target > matrix[MID][n-1]:
                L = MID + 1
            
            else:
                break
        
        if not (L <= R):
            return False
        
        while (l<=r):
            mid = l + (r-l)//2

            if target < matrix[MID][mid]:
                r = mid - 1
            
            elif target > matrix[MID][mid]:
                l = mid + 1
            else:
                return True
        
        return False
                



        