# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        if not s:
            return ""
        
        start_index, end_index = 0, 0
        for i in range(len(s)):
            # odd palindrome
            l1, r1 = expand_from_center(i, i)
            # even palindrome
            l2, r2 = expand_from_center(i, i + 1)
            
            # choose longest palindrome from both expansions
            if (r1 - l1) > (end_index - start_index):
                start_index, end_index = l1, r1
            if (r2 - l2) > (end_index - start_index):
                start_index, end_index = l2, r2

        return s[start_index:end_index+1]