class SkiplistList:
    def __init__(self, limit=100):
        '''Initializes sentinel, height limit, and size.
        '''
        pass
        
    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        pass
    
    def __repr__(self):
        '''Returns a string representation of an object for interactive
        mode.
        '''
        return self.__str__()
        
    def height(self):
        '''Returns the height of the skiplist.
        '''
        pass
        
    def get(self, i):
        '''Returns the element at index i; None if i is inavlid.

        i \in [0,n-1]
        '''
        pass
    
    def set(self, i, x):
        '''Sets the element at valid index i to x and returns the old
        element. Returns None if i is inavlid.

        i \in [0,n-1]
        '''
        pass
    
    def add(self, i, x):
        '''Adds x at valid index i, shifting subsequent elements to the
        right, and returns True. Returns False if i is invalid.

        i \in [0,n]
        '''
        pass
    
    def remove(self, i):
        '''Removes the element at valid index i, shifting subsequent
        elements to the left, and returns the remove elements. Returns 
        None if i is invalid.

        i \in [0,n-1]
        '''
        pass

    def truncate(self, i):
        # As described in Exercise 4.11
        pass

    def absorb(self, l2):
        # As described in Exercise 4.12
        pass
