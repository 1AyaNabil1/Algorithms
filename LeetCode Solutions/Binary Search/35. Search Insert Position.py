def searchInsert(nums, target):
    # Initialize low and high pointers for binary search
    low = 0
    high = len(nums) - 1

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2
        
        # If target is found, return its index
        if nums[mid] == target:
            return mid
        # If target is smaller than mid element, search in left half
        elif nums[mid] > target:
            high = mid - 1
        # If target is larger than mid element, search in right half
        else:
            low = mid + 1
    
    # If target is not found, low will be the correct insertion position
    return low
