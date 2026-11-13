class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        last_pos = -1
        curr_pos = 0
        
        while n > 0:
            if n & 1:
                if last_pos != -1:
                    max_dist = max(max_dist, curr_pos - last_pos)
                last_pos = curr_pos
            curr_pos += 1
            n >>= 1
            
        return max_dist