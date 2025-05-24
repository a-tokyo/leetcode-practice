/**
 * @param {string[]} words
 * @param {character} x
 * @return {number[]}
 */
var findWordsContaining = function(words, x) {
    const result = [];
    words.forEach((word, i) => {
        if (word.includes(x)) {
            result.push(i)
        }
    });
    return result 
};