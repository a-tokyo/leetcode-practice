const romanMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  
  function romanToInt(s: string): number {
    return [...s].reduce((total, ch, i, arr) => {
      const curr = romanMap[ch];
      const next = romanMap[arr[i+1]] || 0;
      // if this symbol is “subtract before larger,” subtract it; otherwise add it
      return total + (curr < next ? -curr : curr);
    }, 0);
  }
  
  // /**
  //  * @param {string} s
  //  * @return {number}
  //  */
  // var romanToInt = function(s) {
  //     let num = 0;
  //     for (let i = 0; i < s.length; i++) {
  //         const currChar = s[i];
  //         let nextChar;
  //         if (i < s.length - 1) {
  //             nextChar = s[i+1];
  //         }
  //         if (nextChar && romanMap[nextChar] > romanMap[currChar]) {
  //             num += romanMap[nextChar] - romanMap[currChar];
  //             i++;
  //         } else {
  //             num += romanMap[currChar];
  //         }
  //     }
  //     return num;
  // };