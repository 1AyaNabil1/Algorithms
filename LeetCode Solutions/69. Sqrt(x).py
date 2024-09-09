def mySqrt(x):
    if x == 0 or x == 1:
        return x  # Square root of 0 and 1 is the number itself
    
    low = 0
    high = x // 2 + 1  # Optimized high bound to reduce search space
    
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid  # Perfect square root found
        elif mid_squared < x:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    
    # Return high as it will be the integer part of the sqrt(x)
    return high
