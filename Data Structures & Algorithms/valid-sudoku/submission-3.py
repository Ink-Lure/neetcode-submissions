class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertBoard = list(zip(*board))
        innerBoard = [['.' for j in range(9)] for i in range(9)]
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                innerBoard[math.floor(j/3) * 3 + math.floor(i/3)][(i % 3) * 3 + (j % 3)] = y

        return self.validBoard(board) and self.validBoard(vertBoard) and self.validBoard(innerBoard)
        
    def validBoard(self, board: List[List[str]]) -> bool:
        for x in board:
            count = Counter(list(x))
            for y, z in zip(count.keys(), count.values()):
                if y.isdigit() and z > 1: return False
        return True
            