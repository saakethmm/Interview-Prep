class Solution {
public:
    void deleteNode(ListNode* node) {
        while (node->next) {
            node->val = node->next->val;
            if (!node->next->next)
                node->next = nullptr;
            else
                node = node->next;
        }
    }
};
