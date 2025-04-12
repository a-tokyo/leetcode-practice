// https://leetcode.com/problems/reverse-integer/

function reverse(x: number): number {
    // use a string hack, no need for modulu math here
    const str = '' + x;
    let result = 0;
    if (str.startsWith('-')) {
      result = Number(str.substring(1).split('').reverse().join('')) * -1;
    } else {
      result = Number(str.split('').reverse().join(''))
    }
      return (result > 2 ** 31 || result < -1 * 2 ** 31) ? 0 : result;
  };