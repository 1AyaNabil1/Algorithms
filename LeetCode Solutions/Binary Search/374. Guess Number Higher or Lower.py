# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the midpoint to avoid overflow
            result = guess(mid)
            
            if result == 0:
                return mid  # We found the pick
            elif result == -1:
                right = mid - 1  # The pick is lower, search in the left half
            else:
                left = mid + 1   # The pick is higher, search in the right half