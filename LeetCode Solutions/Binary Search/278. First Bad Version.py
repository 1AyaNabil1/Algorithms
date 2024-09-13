# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2  # This prevents overflow
            if isBadVersion(mid):
                right = mid  # First bad version might be mid or earlier
            else:
                left = mid + 1  # First bad version is after mid
        return left
