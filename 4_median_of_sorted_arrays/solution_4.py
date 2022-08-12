
class Solution:
    def get_next(self, n1, n2):
        n1_val = None
        n2_val = None
        
        if n1:
            n1_val = n1[0]
        else:
            n1_val = float('inf')
        if n2:
            n2_val = n2[0]
        else:
            n2_val = float('inf')
            
        if n2_val > n1_val:
            n1.pop(0)
            return n1_val
        elif n2_val < float('inf'):
            n2.pop(0)
            return n2_val
        else:
            return 0

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        length = len(nums1) + len(nums2)
        curr_val = None
        k = 0
        
        if length == 1:
            return self.get_next(nums1, nums2)

        while k < length // 2:
            curr_val = self.get_next(nums1, nums2)
            k += 1
            
        if length % 2 == 0:
            next_val = self.get_next(nums1, nums2)
            diff = float(next_val) - float(curr_val)
            return curr_val + (diff / 2)
        else:
            return self.get_next(nums1, nums2)