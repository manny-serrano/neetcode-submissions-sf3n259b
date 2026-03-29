class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # we dont want duplicates in row, or in column so use sets to track both

        rows = defaultdict(set)
        columns = defaultdict(set)

        # to check 3x3 squares, we can make indexes correspond to squares by [0,0][1,0][2,0] etc
        # so set for this will have values[0,0] and on
        squares = defaultdict(set)
        #we know len of board is always 9, and column len as well
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue #continue checking if its empty
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                #if element is already in the row, or column or 3x3 grid, then not valid
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                #update dictionaries with element
        return True
        #valid if not found even after



        