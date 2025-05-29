class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        for ch in magazine:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        for ch in ransomNote:
            if hashmap.get(ch, 0) <= 0:
                return False
            hashmap[ch] = hashmap.get(ch, 0) - 1

        return True
