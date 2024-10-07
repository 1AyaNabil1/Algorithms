class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        diff = (sumAlice - sumBob) // 2

        bobset = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in bobset:
                return[a,b]


# Explanation
# Sum Calculation: We calculate the sum of Alice's and Bob's candy boxes (sumAlice and sumBob).
# Difference Calculation: We compute diff as (sumAlice - sumBob) // 2 to find the value difference needed for balance.
# Set for Fast Lookup: We use a set (bobSet) for bobSizes to quickly check if b = a - diff exists.
# Loop Through Alice's Boxes: For each value a in aliceSizes, we compute b and check if it's in bobSet. If found, we return [a, b].