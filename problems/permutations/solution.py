class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # why 20ms? 別人的solution
        def BT(pos, tmp, ret):
            if len(tmp) == len(nums):
                ret.append(tmp.copy())
                return 
            
            for i in range(pos, len(nums)):
                nums[i], nums[pos] = nums[pos], nums[i]
                tmp.append(nums[pos])
                BT(pos+1, tmp, ret)
                tmp.pop()
                nums[i], nums[pos] = nums[pos], nums[i]
    
        ret = []
        tmp = []
        BT(0, tmp, ret)
        return ret