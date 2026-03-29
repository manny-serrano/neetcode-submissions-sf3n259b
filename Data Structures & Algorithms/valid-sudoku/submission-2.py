class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for rowelement in range(len(board)):
            for columnelement in range (len(board)):
                if board[rowelement][columnelement] == ".":
                    continue
                if (board[rowelement][columnelement] in row[rowelement] or 
                board[rowelement][columnelement] in column[columnelement] or 
                    board[rowelement][columnelement] in square[(rowelement//3, columnelement//3)]):
                    return False
                row[rowelement].add(board[rowelement][columnelement])
                column[columnelement].add(board[rowelement][columnelement])
                square[(rowelement//3, columnelement//3)].add(board[rowelement][columnelement])




        return True


                


        

        
        



        