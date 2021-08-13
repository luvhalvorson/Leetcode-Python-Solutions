class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flags = 0
        col_flags = 0
        for r in range(len(matrix)):    
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row_flags |= (1 << r)
                    col_flags |= (1 << c)
        print(row_flags, col_flags)           
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (row_flags & (1 << r)) or (col_flags & (1 << c)):
                    matrix[r][c] = 0
#         row_flags = [0] * len(matrix)
#         col_flags = [0] * len(matrix[0])
#         for r in range(len(matrix)):    
#             for c in range(len(matrix[0])):
#                 if matrix[r][c] == 0:
#                     row_flags[r] = 1
#                     col_flags[c] = 1
                    
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if row_flags[r] == 1 or col_flags[c] == 1:
#                     matrix[r][c] = 0
              
        