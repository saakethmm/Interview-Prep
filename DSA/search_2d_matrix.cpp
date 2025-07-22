class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int numRows = matrix.size();
        int numCols = matrix[0].size();
        
        int l = 0, h = matrix.size() - 1, mid;
        while (l <= h) {
            mid = (l + h)/2;
            
            if (target < matrix[mid][0])
                h = mid - 1;
            else if (target > matrix[mid][numCols - 1])
                l = mid + 1;
            else
                return binary_search(matrix[mid].begin(), matrix[mid].end(), target);
        }
        return false;
    }
};
