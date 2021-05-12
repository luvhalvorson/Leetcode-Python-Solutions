class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        a = sorted(nums1 + nums2)
        if (m+n) % 2 == 0:
            
            return (a[((m+n)//2)] + a[((m+n)//2) - 1])/2
        else:
            return a[(m+n)//2]