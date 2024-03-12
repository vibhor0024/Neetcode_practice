class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        column = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in rows[r] or \
                board[r][c] in column[c] or \
                board[r][c] in squares[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c])
                column[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True




