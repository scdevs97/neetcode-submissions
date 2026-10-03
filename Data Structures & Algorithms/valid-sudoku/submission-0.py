class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterate through rows
        for i in range(len(board)):
            if self.hasDuplicates(board, (i, 0), (i, 8)):
                return False
    
        #iterate through columns
        for j in range(len(board[0])):
            if self.hasDuplicates(board, (0, j), (8, j)):
                return False

        #iterate through squares
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if self.hasDuplicates(board, (i, j), (i+2, j+2)):
                    print(i, j)
                    return False

        return True

    def hasDuplicates(self, board, startIndex, endIndex):
        start_i = startIndex[0]
        start_j = startIndex[1]
        end_i = endIndex[0]
        end_j = endIndex[1]

        fullSet = set(["1","2","3","4","5","6","7","8","9"])
        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in fullSet:
                    fullSet.remove(board[i][j])
                else:
                    return True
        return False
            