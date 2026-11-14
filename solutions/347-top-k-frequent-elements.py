from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return nlargest(k, count.keys(), key=count.get)