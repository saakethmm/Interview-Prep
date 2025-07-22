class PeekingIterator : public Iterator {
public:
    int prev;
    bool peeked;
	PeekingIterator(const vector<int>& nums) : Iterator(nums), peeked(false) {          
        // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if (!peeked) {
            prev = Iterator::next();
            peeked = true;
        }
        return prev;
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    if (peeked)
            peeked = false;
        else
            prev = Iterator::next();
        return prev;
	}
	
	bool hasNext() const {
        return peeked?true:Iterator::hasNext();
	}
};
