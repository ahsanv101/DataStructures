class SSet:
    def __init__(self):
        '''Initializes member variables.

        >>> sset = SSet()
        '''
        self.sset = []

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> sset = SSet()
        >>> print(sset)  # prints sset.__str__()
        '''
        return str(self.sset)

    def add(self, key, val):
        '''Adds the pair (key, val) to the SSet if no pair with key
        already exists in the SSet, and returns True. Returns False if a
        pair with key already exists in the SSet.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.add(2, 30)
        False
        '''
        for i in range(len(self.sset)):
            if self.sset[i][0] == key:
                return False
        if len(self.sset) != 0:
            for i in range(len(self.sset)):
                if self.sset[i][0] > key:
                    self.sset.insert(i,(key,val))
                    return True
            self.sset.append((key,val))
            return True
        else:
            self.sset.append((key,val))
            return True

    def remove(self, key):
        '''Removes the pair with key from the SSet and returns it.
        Returns None if no such pair exsits.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.remove(1)
        (1, 10)
        >>> sset.remove(10)
        >>>
        '''
        for i in range(len(self.sset)):
            if self.sset[i][0] == key:
                removed = self.sset.pop(i)
                return removed
        return

    def find(self, key):
        '''Returns the pair from the SSet that contains key. If no such
        pair exists, returns the pair from the SSet that contains the
        successor of key. Returns None if no such pair exists.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.find(1)
        (1, 10)
        >>> sset.find(1.5)
        (2, 20)
        >>> sset.find(3)
        >>> 
        '''
        for i in range(len(self.sset)):
            if self.sset[i][0] >= key:
                return self.sset[i]
        return

    def size(self):
        '''Returns the number of pairs currently in the SSet.
        
        >>> sset = SSet()
        >>> sset.size()
        0
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.size()
        2
        >>> sset.add(2, 30)
        False
        >>> sset.size()
        2
        '''
        return len(self.sset)

    def keys(self):
        '''Returns a list of keys in the SSet.
        
        >>> sset = SSet()
        >>> sset.keys()
        []
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.keys()
        [1, 2]
        >>> sset.add(2, 30)
        False
        >>> sset.keys()
        [1, 2]
        '''
        keys = []
        for i in range(len(self.sset)):
            keys.append(self.sset[i][0])
        return keys
