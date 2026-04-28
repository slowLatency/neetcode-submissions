class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort()
        n = len(strs)
        m = len(strs[0])
        i, j, k = 0, 1, 0
        prefix = ""

        while i < m:
            j = 1
            while j < n:
                if i >= len(strs[j]):
                    return prefix
                if strs[0][i] != strs[j][k]:
                    return prefix
                j += 1
            prefix += strs[0][i]
            i += 1
            k += 1
        
        return prefix
