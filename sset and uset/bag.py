from uset import USet

# Adapted from Exercise 1.5 in the book.

class Bag:
    def __init__(self):
        '''Initializes member variables.

        >>> bag = Bag()
        '''
        self.uset = USet()  # this is the underlying data structure.

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> bag = Bag()
        >>> print(bag)  # prints bag.__str__()
        '''
        return str(self.uset)

    def add(self, key, val):
        '''Adds the pair (key, val) to the Bag.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.size()
        1
        >>> bag.add(1, 10)
        >>> bag.size()
        2
        >>> bag.add(1, 20)
        >>> bag.size()
        3
        >>> bag.add(2, 20)
        >>> bag.size()
        4
        '''
        if key in self.uset.keys():
            pair = self.uset.remove(key)
            if isinstance(pair[1],int):
                addingVal = [pair[1]]
            else:
                addingVal = pair[1]
            addingVal.append(val)
            self.uset.add(key,addingVal)
        else:
            self.uset.add(key,val)

    def remove(self, key):
        '''Removes a pair with key from the Bag and returns it.
        Returns None if no such pair exsits.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.remove(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.remove(2)
        (2,20)
        >>> bag.remove(20)
        >>>
        '''
        if key in self.uset.keys():
            values = self.uset.remove(key)[1]
            if isinstance(values,int) == True:
                removed = (key,values)
            else:
                removed = (key,values.pop(0))
            if values == [] or isinstance(values,int) == True:
                return removed
            self.uset.add(key,values)
            return removed
        return

    def find(self, key):
        '''Returns a pair from the Bag that contains key; None if no
        such pair exists.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.find(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.find(2)
        (2,20)
        >>> bag.find(20)
        >>>
        '''
        if key in self.uset.keys():
            values = self.uset.find(key)[1]
            if isinstance(values,int) == True:
                return (key,values)
            else:
                return (key,values[0])
        return

    def size(self):
        '''Returns the number of pairs currently in the Bag.
        
        >>> bag = Bag()
        >>> bag.size()
        0
        >>> bag.add(1, 10)
        >>> bag.add(2, 20)
        >>> bag.size()
        2
        >>> bag.add(2, 30)
        >>> bag.size()
        3
        '''
        size = self.uset.size()
        for key in self.uset.keys():
            values = self.uset.find(key)[1]
            if isinstance(values,int) != True and len(values) > 1:
                size += len(values) - 1
        return size

    def keys(self):
        '''Returns a list of keys in the Bag.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.keys()
        [1, 2]
        '''
        return self.uset.keys()

    def find_all(self,key):
        valList = []
        if key in self.uset.keys():
            values = self.uset.find(key)[1]
            if isinstance(values,int) == True:
                valList.append((key,values))
            else:
                for i in values:
                    valList.append((key,i))
        return valList