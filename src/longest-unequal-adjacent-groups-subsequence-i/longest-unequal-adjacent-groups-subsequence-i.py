class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        result = [words[0]]
        for i in range(1, len(words)):
            if groups[i] != groups[i-1]:
                result += [words[i]]
        return result