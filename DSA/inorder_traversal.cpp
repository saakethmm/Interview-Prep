/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> vals;
        inorder(root, vals);
        return vals;
    }
private:
    void inorder(TreeNode* node, vector<int> &vals) {
        if (!node)
            return;
        inorder(node->left, vals);
        vals.push_back(node->val);
        inorder(node->right, vals);
    }
};
