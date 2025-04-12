// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// https://leetcode.com/submissions/detail/1604458045/

function lengthOfLongestSubstring(s) {
    // loop over string -- keep track of max 
    let max_so_far = ''
    let current_max = '';
    for (let i = 0; i <= s.length; i++) {
      const char = s.charAt(i);
      if (current_max.includes(char)) {
          max_so_far = max_so_far.length > current_max.length ? max_so_far : current_max;
          if (i > 1) {
              current_max = s.substring(s.substring(0, i).lastIndexOf(s.charAt(i)) + 1, i + 1);
          } else {
              current_max = char;
          }
      } else {
          current_max+=char;
      }
    }
    return max_so_far.length;
  };