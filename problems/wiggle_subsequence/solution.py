class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_len = len(nums)
        up = [0 for _ in range(nums_len)]
        down = [0 for _ in range(nums_len)]

        up[0] = 1
        down[0] = 1

        for i in range(1, nums_len):
            prev = nums[i - 1]
            curr = nums[i]

            if prev < curr:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif prev > curr:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                # prev == curr:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[nums_len - 1], down[nums_len - 1])
                    
            
                    