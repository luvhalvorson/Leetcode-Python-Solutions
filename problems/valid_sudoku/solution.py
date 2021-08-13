class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] *9
        col = [0] *9
        box = [0] *9
        for r in range(9):
            for c in range(9):
                
                e = board[r][c]
                if e == ".":
                    continue
                pos = int(e) - 1
                
                if row[r] & (1 << pos):
                    return False
                else:
                    row[r] |= (1 << pos)
                if col[c] & (1 << pos):
                    return False
                else:
                    col[c] |= (1 << pos)
                    
                idx = r // 3 * 3 + c // 3
                if box[idx] & (1 << pos):
                    return False
                else:
                    box[idx] |= (1 << pos)
        return True
                
#         col_arr = [[0] * 9 for _ in range(9)]
#         square_arr = [[0] * 9 for _ in range(9)]
        
#         for row_i, row in  enumerate(board):
#             row_arr = [0] *9
#             for col_i, col in enumerate(row):
#                 if col is ".":
#                     continue
#                 if row_arr[int(col) - 1] != 0 or col_arr[col_i][int(col) - 1] != 0 or square_arr[row_i // 3 * 3 + col_i // 3][int(col) - 1] != 0:
#                     return False
#                 else:
#                     row_arr[int(col) - 1] = 1
#                     col_arr[col_i][int(col) - 1] = 1 
#                     square_arr[row_i // 3 * 3 + col_i // 3][int(col) - 1] = 1
#         return True
#         square_dic = [[set() for _ in range(3)] for _ in range(3)]
#         col_dic = [set() for _ in range(9)]
        
#         for row_i, row in  enumerate(board):
#             row_dic = set()
#             for col_i, col in enumerate(row):
#                 if col is ".":
#                     continue
#                 if (col in row_dic) or (col in col_dic[col_i]) or (col in square_dic[col_i // 3][row_i // 3]):
                    
#                     return False
#                 else:
#                     col_dic[col_i].add(col)
#                     row_dic.add(col)
#                     square_dic[col_i // 3][row_i // 3].add(col)
        
#         return True
                