from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(30, -1, -1):
            mask |= (1 << i)
            found = {num & mask for num in nums}
            
            greedy = max_xor | (1 << i)
            for prefix in found:
                if greedy ^ prefix in found:
                    max_xor = greedy
                    break
                    
        return max_xor