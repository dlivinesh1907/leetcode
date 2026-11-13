class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        from collections import Counter
        count = Counter(s1.split()) + Counter(s2.split())
        return [word for word, freq in count.items() if freq == 1]