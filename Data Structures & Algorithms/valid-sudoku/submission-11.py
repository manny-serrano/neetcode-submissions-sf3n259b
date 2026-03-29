class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input is sixe nxn -> longest being 9, so highest is 81
        # chars in lists, 
        # output is boolean true or false
        # can do 2^n, n! n^2
        #2d matrix problem, validation problem so checking not optimizing
        # without duplicates, use hashsets or hashmaps


        rows = defaultdict(set)
        columns = defaultdict(set)
        grids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in grids[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                grids[(r//3, c//3)].add(board[r][c])
        return True 
        







                
        