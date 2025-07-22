class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        if (!head)
            return false;
        
        ListNode *s = head;
        ListNode *f = head->next;
        while (f && f->next) {
            if (f == s)
                return true;
            s = s->next;
            f = f->next->next;
        }
        return false;
    }
};
