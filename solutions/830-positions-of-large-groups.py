class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        n = len(s)
        start = 0
        
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if i - start + 1 >= 3:
                    result.append([start, i])
                start = i + 1
                
        return result