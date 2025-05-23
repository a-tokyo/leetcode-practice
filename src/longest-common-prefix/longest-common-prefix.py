class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''

        while True:
            for i in range(len(strs)):
                if len(strs[i]) <= len(lcp) or strs[i][len(lcp)] != strs[0][len(lcp)]:
                    return lcp
            lcp+=strs[0][len(lcp)]

        return lcp