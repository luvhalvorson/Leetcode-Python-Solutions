class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        ## 試試看別人的扣
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if m<=0:
            nums1[:n]=nums2[:n]
#         if m == 0:
#             #nums1 =  nums2 # pass by copy of reference, doensnt workhere
#             nums1[:] = nums2
#             return # 可直接回去了
#         if n == 0:
#             return
#         nums1[len(nums1) - m:] = nums1[:m].copy()
#         nums1[:len(nums1) - m] = [0] * (len(nums1) - m) # 不能甜*m
        
#         p1, p2 = len(nums1) - m, 0
#         curpos = 0
        
#         while p1 < len(nums1) and p2 < n:
#             if nums1[p1] < nums2[p2]:
#                 nums1[curpos] = nums1[p1]
#                 curpos += 1
#                 p1 += 1
#             elif nums1[p1] > nums2[p2]:
#                 nums1[curpos] = nums2[p2]
#                 curpos += 1
#                 p2 += 1
        
#             else:
#                 nums1[curpos] = nums2[p2]
#                 curpos += 1
#                 nums1[curpos] = nums1[p1]
#                 curpos += 1
#                 p1 += 1
#                 p2 += 1
                
#         if p2 < n:
#             nums1[curpos:] = nums2[p2:]
        
        
        
        
        