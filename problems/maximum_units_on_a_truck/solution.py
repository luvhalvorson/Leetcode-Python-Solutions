class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sl = sorted(boxTypes, key = lambda x: x[1], reverse=True)
        print(sl)
        res = 0
        for box in sl:
            usebox =  min(truckSize, box[0])
            res += usebox * box[1]
            truckSize -=  usebox
            if truckSize == 0:
                break
        return res