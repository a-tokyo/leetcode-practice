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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (!root) return false;

    const stack: [TreeNode, number][] = [[root, root.val]];

    while(stack.length) {
        const [node, sum] = stack.pop();

        if (!node.left && !node.right) {
            if (sum === targetSum) return true;
            continue;
        } else {
            if (node.left) stack.push([node.left, sum + node.left.val]);
            if (node.right) stack.push([node.right, sum + node.right.val]);
        }
    }

    return false;
};