from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Count elements in nums1
        count = Counter(nums1)
        
        # Step 2: Initialize the result list
        result = []
        
        # Step 3: Iterate over nums2 and collect common elements
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1  # Decrement the count of the element in the hash map
        
        return result