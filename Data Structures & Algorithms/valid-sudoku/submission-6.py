class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # want to check each row, column and grid region
        # each 3x3 can be a dict of sets with r//3 c//3
        # boardhas r and c coordinate
        #initiate

        rows = defaultdict(set) #will just hold set of 
        columns = defaultdict(set)
        squares = defaultdict(set)

        #iterate through each individual region
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue #empty
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
        