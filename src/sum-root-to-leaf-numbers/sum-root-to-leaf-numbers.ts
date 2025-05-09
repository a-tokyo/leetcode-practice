/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumNumbers(root: TreeNode | null): number {
    if (!root) return 0;

    const nodeStack = [root];
    const valStack = [root.val];
    let sum = 0;

    while (nodeStack.length) {
        const node = nodeStack.pop();
        const value = valStack.pop();

        const { left, right } = node;
        if (!left && !right) {
            sum += value;
        } else {
            if (left) {
                nodeStack.push(left);
                valStack.push(10 * value + left.val);
            }
            if (right) {
                nodeStack.push(right);
                valStack.push(10 * value + right.val);
            }
        }
    }
    return sum;
}