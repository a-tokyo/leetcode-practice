function exist(board: string[][], word: string): boolean {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(i: number, j: number, k: number, visited: Set<string>): boolean {
        if (k === word.length) return true;

        if (
            i < 0 || i >= rows ||
            j < 0 || j >= cols ||
            board[i][j] !== word[k] ||
            visited.has(`${i},${j}`)
        ) {
            return false;
        }

        const newVisited = new Set(visited);
        newVisited.add(`${i},${j}`);

        return (
            dfs(i + 1, j, k + 1, newVisited) ||
            dfs(i - 1, j, k + 1, newVisited) ||
            dfs(i, j + 1, k + 1, newVisited) ||
            dfs(i, j - 1, k + 1, newVisited)
        );
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (dfs(i, j, 0, new Set())) {
                return true;
            }
        }
    }

    return false;
};