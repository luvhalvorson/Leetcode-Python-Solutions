class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = [1] * len(ratings)
        r2l = [1] * len(ratings)
        for i in range(len(ratings) - 1):
             if ratings[i] < ratings[i+1] and l2r[i+1] <= l2r[i]:
                    l2r[i+1] = l2r[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
             if ratings[i-1] > ratings[i] and r2l[i-1] <= r2l[i]:
                    r2l[i-1] = r2l[i] + 1
        
        
        print(l2r, "n", r2l)
        return sum(map(max, zip(l2r, r2l)))