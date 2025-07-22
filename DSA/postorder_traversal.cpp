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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> vals;
        postorder(root, vals);
        return vals;
    }
private:
    void postorder(TreeNode* node, vector<int> &vals) {
        if (!node)
            return;
        postorder(node->left, vals);
        postorder(node->right, vals);
        vals.push_back(node->val);
    }
};
