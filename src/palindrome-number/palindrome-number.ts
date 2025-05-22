function isPalindrome(x: number): boolean {
    const s = String(x);
    return s === [...s].reverse().join('');
};