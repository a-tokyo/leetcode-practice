// https://leetcode.com/problems/longest-palindromic-substring/
// https://leetcode.com/submissions/detail/1604517121/

function longestPalindrome(s: string): string {
    function expandFromCenter(left: number, right: number) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            left--;
            right++;
        }
        return [left + 1, right - 1];
    }

    if (!s) return "";

    let startIndex = 0;
    let endIndex = 0;

    for (let i = 0; i < s.length; i++) {
        // odd-length palindrome
        const [l1, r1] = expandFromCenter(i, i);
        // even-length palindrome
        const [l2, r2] = expandFromCenter(i, i + 1);

        if ((r1 - l1) > (endIndex - startIndex)) {
            startIndex = l1;
            endIndex = r1;
        }
        if ((r2 - l2) > (endIndex - startIndex)) {
            startIndex = l2;
            endIndex = r2;
        }
    }

    return s.substring(startIndex, endIndex + 1);
};