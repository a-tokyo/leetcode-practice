/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const n = matrix.length;
    const m = matrix[0].length;

    let rowZero = matrix[0].some(value => value === 0);
    let colZero = matrix.some(row => row[0] === 0);

    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            if (matrix[i][j] === 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    for (let i = 1; i < n; i++) {
        for (let j = 1; j < m; j++) {
            if (matrix[0][j] === 0 || matrix[i][0] === 0) {
                matrix[i][j] = 0;
            }
        }
    }

    if (rowZero) {
        for (let j = 0; j < m; j++) {
            matrix[0][j] = 0;
        }
    }

    if (colZero) {
        for (let i = 0; i < n; i++) {
            matrix[i][0] = 0;
        }
    }
}