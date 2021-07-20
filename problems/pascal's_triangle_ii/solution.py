class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        for i in range(2, rowIndex + 1):
            for j in range(len(res) - 2 + 1):
                res[j] = sum(res[j : j+2])
            #print(res)
            res = [1] + res[:-1] + [1]
        return res
        # lastrow = self.getRow(rowIndex - 1)
        # return [1] + [sum(lastrow[i: i+2]) for i in range(len(lastrow) - 2 + 1)] + [1]

       