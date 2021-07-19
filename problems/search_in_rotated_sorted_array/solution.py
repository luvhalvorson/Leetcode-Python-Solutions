class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # 要跟 nums[r]比較，r只能是len(nums) -1
        while l < r: #找到唯一最小的 怎麼知道會斷在l ==r時
            mid = l + (r - l) // 2
            if nums[mid]  < nums[r]:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            return l
        rot = l
        l, r = 0, len(nums)
        while l < r:
            mid = (l + (r - l) // 2)
            realmid = (mid + rot) % len(nums)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                l = mid + 1
            else:
                r = mid
        return -1