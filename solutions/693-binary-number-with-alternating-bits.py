class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= n >> 2
        return (n & (n - 1)) == 0