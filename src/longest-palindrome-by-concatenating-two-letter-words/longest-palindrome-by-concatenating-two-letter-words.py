from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        left = ''
        middle = ''
        right = ''
        hashtable = {}

        for word in words: hashtable[word] = hashtable.get(word, 0) + 1

        for word in hashtable:
            count = hashtable[word]
            if count == 0:
                continue

            complement = word[::-1]

            if word == complement:
                pair_count = count // 2
                left += word * pair_count
                right = word * pair_count + right
                if middle == '' and count % 2 == 1:
                    middle = word
                hashtable[word] = 0
            else:
                if complement in hashtable and hashtable[complement] > 0:
                    pair_count = min(count, hashtable[complement])
                    left += word * pair_count
                    right = complement * pair_count + right
                    hashtable[word] = 0
                    hashtable[complement] = 0
        
        return len(left + middle + right)

#---#

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        length = 0
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        middle = False
        for word in freq:
            count = freq[word]
            if count == 0:
                continue

            complement = word[::-1]

            if word == complement:
                pair_count = count // 2
                length += pair_count * 4
                if not middle and count % 2 == 1:
                    length += 2
                    middle = True
                freq[word] = 0
            else:
                if complement in freq and freq[complement] > 0:
                    pair_count = min(count, freq[complement])
                    length += pair_count * 4
                    freq[word] = 0
                    freq[complement] = 0
        
        return length