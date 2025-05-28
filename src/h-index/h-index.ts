function hIndex(citations: number[]): number {
    citations.sort((a,b) => b-a); // note that the default sort and reverse in JS wont work as it does in py.
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] <= i) return i
    }
    return citations.length
};