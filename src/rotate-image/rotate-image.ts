/**
 Do not return anything, modify matrix in-place instead.
 */
 function rotate(matrix: number[][]): void {
    // find transpose
    for (let i = 0; i < matrix.length; i++) {
        for (let j = i+1; j < matrix.length; j++) {
            if (i == j) {
                continue;
            }
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    // reverse row order
    for (let i = 0; i < matrix.length; i++) {
        matrix[i] = matrix[i].reverse()
    }
};