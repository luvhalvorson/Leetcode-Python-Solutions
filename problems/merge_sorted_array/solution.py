class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[::] = nums2
            
            return
        if n == 0:
            return
        nums1[n:] = nums1[:m].copy()
        #print(nums1)
        i , p1, p2 = 0, 0, 0
        while p1 < m and p2 < n:
            print(nums1)
            if nums1[n + p1] < nums2[p2]:
                nums1[i] = nums1[n + p1] 
                p1 += 1
            elif nums1[n + p1] >= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 += 1
            i+=1
        #print(p1, p2)
        if p2 < n :
            nums1[i:] = nums2[p2:] 
        