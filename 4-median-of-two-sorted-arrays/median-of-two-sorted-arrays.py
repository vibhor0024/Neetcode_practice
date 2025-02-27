class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        l = 0
        r = len(nums1) - 1

        while True:

            i = l + (r-l) // 2
            j = half - i - 2

            nums1left = nums1[i] if i>=0 else float('-infinity')
            nums1right = nums1[i+1] if i < len(nums1)-1 else float('+infinity')
            nums2left = nums2[j] if j>=0 else float('-infinity')
            nums2right = nums2[j+1] if j < len(nums2)-1 else float('+infinity')

            
            if nums1left <= nums2right and nums2left <= nums1right:
                if total%2 == 1:
                    return min(nums1right,nums2right)
                else:
                    return (min(nums1right,nums2right)+ max(nums1left,nums2left))/2
            
            elif nums1left > nums2right:
                r = i - 1
            else:
                l = i + 1
            
