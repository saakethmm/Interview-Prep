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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> vals;
        preorder(root, vals);
        return vals;
    }
private:
    void preorder(TreeNode* node, vector<int> &vals) {
        if (!node)
            return;
        vals.push_back(node->val);
        preorder(node->left, vals);
        preorder(node->right, vals);
    }
};
