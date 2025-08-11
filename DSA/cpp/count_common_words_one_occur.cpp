class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        unordered_map<string, int> counts1;
        unordered_map<string, int> counts2;
        int total = 0;

        for (string &word : words1) {
            counts1[word]++;
        }
        
        for (string &word: words2) {
            counts2[word]++;
            
        }
        
        if (words1.size() > words2.size()) {
            for (string &word : words2) {
                if (counts1[word] == 1 && counts2[word] == 1) 
                    total++;
            }
        }
        else {
            for (string &word : words1) {
                if (counts1[word] == 1 && counts2[word] == 1) 
                    total++;
            }
        }

        return total;
    }
};
