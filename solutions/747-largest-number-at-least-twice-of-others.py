class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = -1
        max_idx = -1
        second_max = -1
        
        for i, num in enumerate(nums):
            if num > max_val:
                second_max = max_val
                max_val = num
                max_idx = i
            elif num > second_max:
                second_max = num
                
        if max_val >= 2 * second_max:
            return max_idx
        return -1