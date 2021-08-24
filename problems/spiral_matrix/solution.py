class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] #u + 1 r-1 low-1 l+1
        curi, curj = 0, 0
        curd = 0
        res = []
        upperbound, lowerbound = 0, m
        leftbound, rightbound = 0, n
        
        while upperbound < m and lowerbound >= 0 and leftbound < n and rightbound >=0:
            #print("meow", upperbound, lowerbound,leftbound,  rightbound)
            #print(curi, curj)
            
            while upperbound <= curi < lowerbound and leftbound <= curj < rightbound:
                res.append(matrix[curi][curj])
                curi += directions[curd][0]
                curj += directions[curd][1]
            curi -= directions[curd][0]
            curj -= directions[curd][1]
            #print(curi, curj, curd)
            if curd == 0:
                upperbound += 1
            if curd == 1:
                rightbound -= 1
            if curd == 2:
                lowerbound -= 1
            if curd == 3:
                leftbound += 1
            
            curd = (curd + 1) % 4
            curi += directions[curd][0]
            curj += directions[curd][1]

        return res