/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private TreeNode ans = null;
    
    public boolean dfs(TreeNode n, TreeNode p, TreeNode q) {
        if (n == null) return false;
        int l = dfs(n.left, p, q) ? 1 : 0;
        int r = dfs(n.right, p, q) ? 1 : 0;
        int mid = (n == p || n == q) ? 1 : 0;
        if (l + r + mid == 2)
            ans = n;
        return (l + r + mid > 0);
    }
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        dfs(root, p, q);
        return ans;
    }    
}
