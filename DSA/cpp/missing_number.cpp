class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int part = 0;
        for (int i : nums) {
            part += i;
        }
        int s = nums.size();
        return s*(s+1)/2-part;
    }
};
