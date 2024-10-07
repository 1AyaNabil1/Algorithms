from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def countSoldiers(row):
            # Binary search to find the first 0 in the row
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # Create a list of (number of soldiers, row index) pairs
        soldier_counts = [(countSoldiers(row), i) for i, row in enumerate(mat)]
        
        # Sort by number of soldiers, and by row index in case of a tie
        soldier_counts.sort()
        
        # Return the indices of the first k rows
        return [index for _, index in soldier_counts[:k]]