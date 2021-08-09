class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s_i = sorted(intervals)
        res = [s_i[0]]
        for interval in s_i[1:]:
            if res[-1][0] <= interval[0] <= res[-1][1] :
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res