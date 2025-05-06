// https://leetcode.com/problems/string-to-integer-atoi/description/

const INT_MAX = 2**31 - 1;
const INT_MIN = -(2**31);

var myAtoi = function(s) {
  let i = 0;
  let n = s.length;
  let sign = 1;
  let num = 0;

  // skip leading spaces (no full trim)
  while (i < n && s[i] === ' ') i++;
  
  // optional sign
  if (i < n && (s[i] === '+' || s[i] === '-')) {
    if (s[i] === '-') sign = -1;
    i++;
  }

  // parse digits and clamp on the fly
  while (i < n) {
    const c = s[i];
    if (c < '0' || c > '9') { 
        break;
    }
    const digit = c.charCodeAt(0) - 48;
    // overflow check
    if (num > Math.floor(INT_MAX/10) ||
       (num === Math.floor(INT_MAX/10) && digit > INT_MAX % 10)) {
      return sign === 1 ? INT_MAX : INT_MIN;
    }

    num = num * 10 + digit;
    i++;
  }
  return sign * num;
};