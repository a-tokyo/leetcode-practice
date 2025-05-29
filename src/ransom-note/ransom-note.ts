function canConstruct(ransomNote: string, magazine: string): boolean {
    const hashmap: Record<string, number> = {};
    for (const ch of magazine) {
        hashmap[ch] = (hashmap[ch] || 0) + 1;
    }
    for (const ch of ransomNote) {
        if (!hashmap[ch]) {
            return false;
        }
        hashmap[ch]--;
    }
    return true;
}