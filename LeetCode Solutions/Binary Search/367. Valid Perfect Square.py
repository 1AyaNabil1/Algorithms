class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1
                
        return False