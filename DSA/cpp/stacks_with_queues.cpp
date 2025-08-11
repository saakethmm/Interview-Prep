#include <queue>

class MyStack {
    std::queue<int> q1;
    std::queue<int> q2;
public:
    MyStack() {
    }
    
    void push(int x) {
        q1.push(x);
        while(!q2.empty()) {
            q1.push(q2.front());
            q2.pop();
        }
        
        q2 = q1;
        while(!q1.empty()) {
            q1.pop();
        }
    }
    
    int pop() {
        int t = q2.front();
        q2.pop();
        return t;
    }
    
    int top() {
        return q2.front();
    }
    
    bool empty() {
        return q2.empty();
    }
};
