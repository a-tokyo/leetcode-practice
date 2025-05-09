/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = (s) => {
    if (s.length & 1) {
      return false;
    }
  
    const match = new Map([
      [')', '('],
      [']', '['],
      ['}', '{']
    ]);
    const stack = [];
  
    for (const currChar of s) {
      if (!match.has(currChar)) {
        stack.push(currChar);
        continue;
      }
  
      if (stack.pop() !== match.get(currChar)) {
          return false;
      }
    }
  
    return stack.length == 0;
  };