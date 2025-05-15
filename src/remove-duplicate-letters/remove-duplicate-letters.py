class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        used = set()
        # mantain max index of each actual element
        max_indices = {}
        for i in range(n):
            max_indices[s[i]] = i

        # mantains next smaller index
        stack = []
        for i in range(n):
            if s[i] in used: continue
            while stack and stack[-1] > s[i] and max_indices[stack[-1]] > i:
                used.remove(stack[-1])
                curr = stack.pop()
            stack.append(s[i])
            used.add(s[i])

        return "".join(stack)
