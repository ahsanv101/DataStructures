from dl_list import DLList

class MinDeque:
    '''As described in Exercise 3.16.'''

    def __init__(self):
        """Initializing its members
        """
        self.list = DLList()
        self.min = []

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return str(self.list)

    def add_first(self, x):
        '''Adds x at the front.
        '''
        self.list.add(0,x)
        if self.min == []:
            self.min.append(x)
        else:
            while self.min[-1] > x and self.min != []:
                self.min.pop(-1)
            self.min[-1] = x

    def add_last(self, x):
        '''Adds x at the back.
        '''
        self.list.add(-1,x)
        if self.min == []:
            self.min.append(x)
        else:
            while self.min[-1] > x and self.min != []:
                self.min.pop(-1)
            self.min[-1] = x

    def remove_first(self):
        '''Removes the element at the front and returns it. Returns None
        if dq is empty.
        '''
        if self.min != [] and self.min[0] == self.list.get(0):
            self.min.pop(0)
        return self.list.remove(0)

    def remove_last(self):
        '''Removes the element at the back and returns it. Returns None 
        if dq is empty.
        '''
        if self.min != [] and self.min[0] == self.list.get(-1):
            self.min.pop(0)
        return self.list.remove(-1)

    def size(self):
        '''Returns the number of elements currently in the dq.
        '''
        return self.list.size

    def min(self):
        '''Returns the smallest element currently in the dq.
        '''
        return min[0]

    
