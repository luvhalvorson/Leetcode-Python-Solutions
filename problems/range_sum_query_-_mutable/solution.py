class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        blocksize =  int(math.sqrt(len(nums)))
        blocksum = []
        for i in range(0, len(nums), blocksize):
            blocksum.append(sum(nums[i: i + blocksize]))
        
        self.blocksize = blocksize
        self.blocksum = blocksum
    def update(self, index: int, val: int) -> None:
        blocksize = self.blocksize
        block = index // blocksize
        
        oval = self.nums[index] 
        self.nums[index] = val
        self.blocksum[block] += (- oval + val)
        #print(self.nums, self.blocksum)

    def sumRange(self, left: int, right: int) -> int:
        blocksize = self.blocksize
        l_block = left // blocksize
        r_block = right // blocksize
        blocksum = self.blocksum
        nums = self.nums
        if l_block == r_block:
            
            return sum(nums[left:right+1])
        else:
            l_ofst = left % blocksize
            r_ofst = right % blocksize
            ls = sum(nums[left:left+blocksize-l_ofst]) if l_ofst != 0 else blocksum[l_block]
            rs = sum(nums[r_block*blocksize:right+1]) if r_ofst != blocksize-1 else blocksum[r_block]
            return  ls + sum(blocksum[l_block+1 : r_block]) + rs
        
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)