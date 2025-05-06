what about now

/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    let str = s.trim();
    let signMultiplier = 1;
    if (!str.length) {
        return 0;
    }
    if (str.startsWith('-')) {
        signMultiplier = -1;
        str = str.substring(1);
    } else if (str.startsWith('+')){
        str = str.substring(1);
    }

    let numberSoFarStr = '';

    const firstPeriodIndex = str.indexOf('.')
    for (let i=0; i < str.length; i++) {
        const currChar = str[i];
        const currNum = Number(currChar);
        if ((currChar === ' ' || isNaN(currNum)) || (currChar === '.' && i !=firstPeriodIndex)) {
            break;
        }
        // here we have a char to be added to the num string
        numberSoFarStr = `${numberSoFarStr}${currChar}`
    }

    // handle rounding
    const finalNum = Number(numberSoFarStr || 0) * signMultiplier;
    if (finalNum < -1 * 2**31) {
        return -1 * 2**31;
    } else if (finalNum >  2**31 - 1) {
        return 2**31 - 1;
    }
    return finalNum;
};