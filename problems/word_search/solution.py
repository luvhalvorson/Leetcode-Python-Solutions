
class Solution:    
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        n = len(board)
        m = len(board[0])
        
        def check_word(x, y, ind):
            if board[x][y] == '0':
                return False
            
            if ind == word_len:
                return True
                
            board[x][y] = chr(ord(board[x][y]) + 42)
            
            move = False
            if y - 1 >= 0 and board[x][y-1] == word[ind]:
                if check_word(x, y - 1, ind + 1):
                    return True
                move = True
            
            if y + 1 < m and board[x][y + 1] == word[ind]:
                if check_word(x, y + 1, ind + 1):
                    return True
                move = False
                
            if x + 1 < n and board[x + 1][y] == word[ind]:
                if check_word(x + 1, y, ind + 1):
                    return True
                move = False
                
            if x - 1 >= 0 and board[x - 1][y] == word[ind]:
                if check_word(x - 1, y, ind + 1):
                    return True
                move = False
                
            if not move:
                board[x][y] = chr(ord(board[x][y]) - 42)
                
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if check_word(i, j, 1):
                        return True
                
                for x in range(n):
                    for y in range(m):
                        if ord(board[x][y]) > ord("z"):
                            board[x][y] = chr(ord(board[x][y]) - 42)
        return False