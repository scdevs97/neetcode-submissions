class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVals = [0] * 9
        colVals = [0] * 9
        squareVals = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                if ((1 << val) & rowVals[r]) or ((1 << val) & colVals[c]) or ((1 << val) & squareVals[(r // 3) * 3 + (c // 3)]):
                    return False
                
                rowVals[r] |= (1 << val)
                colVals[c] |= (1 << val)
                squareVals[(r // 3) * 3 + (c // 3)] |= (1 << val)
        
        return True