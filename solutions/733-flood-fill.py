class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        
        m, n = len(image), len(image[0])
        
        def dfs(r, c):
            if image[r][c] == orig_color:
                image[r][c] = color
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < m:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < n:
                    dfs(r, c + 1)
                    
        dfs(sr, sc)
        return image