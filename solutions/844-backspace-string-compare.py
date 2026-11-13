class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_valid_char_index(string, index):
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1
                    index -= 1
                elif backspace_count > 0:
                    backspace_count -= 1
                    index -= 1
                else:
                    break
            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = get_next_valid_char_index(s, i)
            j = get_next_valid_char_index(t, j)

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True