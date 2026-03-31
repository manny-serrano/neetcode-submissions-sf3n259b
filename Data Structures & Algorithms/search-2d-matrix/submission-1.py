class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l,r = 0, len(matrix)*len(matrix[0]) - 1

        while l<=r:
            middle = l + (r-l)//2
            row, col = middle // len(matrix[0]), middle % len(matrix[0])
            if target>matrix[row][col]:
                l = middle + 1
            elif target < matrix[row][col]:
                r = middle -1
            else:
                return True 
        return False
        