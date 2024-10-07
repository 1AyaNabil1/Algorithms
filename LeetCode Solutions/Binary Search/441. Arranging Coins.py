class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left) // 2
            current_sum = mid * (mid + 1) // 2  # Sum of the first `mid` rows
            
            if current_sum == n:
                return mid  # Exact match
            elif current_sum < n:
                left = mid + 1  # Try for a larger `k`
            else:
                right = mid - 1  # Try for a smaller `k`
        
        return right  # `right` will be the largest `k` where sum <= n