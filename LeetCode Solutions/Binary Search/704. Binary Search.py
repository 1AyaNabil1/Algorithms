class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            # Check if the middle element is the target
            guess = nums[mid]
            if guess == target:
                return mid
            # If target is greater, ignore the left half
            elif guess < target:
                left = mid + 1
            # If target is smaller, ignore the right half
            else:
                right = mid - 1
        
        # Target not found
        return -1