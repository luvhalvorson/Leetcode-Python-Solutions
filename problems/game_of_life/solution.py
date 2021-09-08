class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #1 -> 1  2or3
        #0 -> 1  3 1
        res = [[0]*len(board[0]) for _ in range(len(board))]
        for m in range(len(board)):
            for n in range(len(board[0])):
                cursum = 0
               
                if m > 0:
                    cursum += board[m - 1][n]
                if n > 0:
                    cursum += board[m][n - 1]                    
                if m > 0 and n > 0:
                    cursum += board[m - 1][n - 1]                
                if m > 0 and n < len(board[0]) - 1:
                    cursum += board[m - 1][n + 1]                   
                if m < len(board) - 1 and n > 0:
                    cursum += board[m + 1][n - 1]
                if m < len(board) - 1:
                    cursum += board[m + 1][n]
                if n < len(board[0]) - 1:
                    cursum += board[m][n + 1]
                if m < len(board) - 1 and n < len(board[0]) - 1:
                    cursum += board[m + 1][n + 1]

                
                if board[m][n] == 1:
                    if 2 <= cursum <= 3:
                        res[m][n] = 1
                else:
                    if cursum == 3:
                        res[m][n] = 1
        for m in range(len(board)):
            for n in range(len(board[0])):
                board[m][n] = res[m][n]