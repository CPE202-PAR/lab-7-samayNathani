
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap = [0]
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        self.heap.append(item)
        self.size +=1
        self.perc_up(self.size)
        return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        return self.heap[1]


    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        maxVal = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size-=1
        self.heap.pop()
        self.perc_down(1)
        return maxVal

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap[1:]


    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from 
        the items in alist using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        i = len(alist)//2
        self.size = len(alist)
        if self.capacity < self.size:
            self.capacity = self.size
        self.heap = [0] + alist
        while i > 0:
            self.perc_down(i)
            i-=1

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.size == 0


    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.size == self.capacity

        
    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size

        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i*2 <= self.size:
            maxChild = self.maxChild(i)
            if self.heap[i] < self.heap[maxChild]:
                temp = self.heap[i]
                self.heap[i] = self.heap[maxChild]
                self.heap[maxChild] = temp
            i = maxChild

    def maxChild(self, i):
        if i*2+1 > self.size:
            return i*2
        else:
            if self.heap[i*2+1] < self.heap[i*2]:
                return i*2
            else:
                return i*2+1

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i-1)//2 >= 1:
            if self.heap[i] > self.heap[i//2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = temp
            i//=2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        self.build_heap(alist)
        while self.size > 0:
            maxVal = self.dequeue()
            alist[self.size] = maxVal