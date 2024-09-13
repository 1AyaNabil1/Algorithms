class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Step 1: Convert both arrays to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Step 2: Find the intersection of the two sets
        result = set1 & set2  # or set1.intersection(set2)