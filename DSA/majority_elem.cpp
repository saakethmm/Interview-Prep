class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int most = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (most != nums[i]) {
                --count;
                if (count == 0) {
                    most = nums[i];
                    ++count;
                }
            }
            else {
                ++count;
            }
            cout << most << endl;
        }
        return most;
    }
};
