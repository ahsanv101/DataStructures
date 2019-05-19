class DLNode:
    def __init__(self, data):
        self.data = data
        self.front = self.back = None

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        return str(self.data)

class DLList:
    def __init__(self):
        '''Initializes the dummy node and size.'''
        self.dummy = DLNode(None)
        self.size = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        if self.size == 0:
            return (self.dummy)
        else:
            lst = []
            currentNode = self.dummy
            for i in range(self.size):
                currentNode = currentNode.front
                lst.append(currentNode.data)
            return str(lst)

    def get(self, i):
        '''DL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        return self.get_node(i).data

    def get_node(self, i):
        '''
        Gets the node at the ith index
        '''
        if i > self.size or i < (-1*self.size):
            return
        else:
            if i < 0:
                i = i % self.size
            if i < self.size/2:
                currentNode = self.dummy.front      #if index is within first half of the list, iterate from the front
                while (i != 0):
                    currentNode = currentNode.front
                    i -= 1
            else:
                currentNode = self.dummy.back       #if index is within second half of the list, iterate from the back
                # to ensure list is iterated only n-i times and since 1 node has already been counted, 1 is also subtracted
                i = self.size - i - 1
                while (i != 0):
                    currentNode = currentNode.back
                    i -= 1
        return currentNode

    def set(self, i, x):
        '''DL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i > self.size or i < (-1 * self.size):
            return False
        else:
            currentNode = self.get_node(i)
            currentNode.data = x
            return True

    def add(self, i, x):
        '''DL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {-n, ... , n}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i > self.size or i < -1*(self.size):         #checking i is outside the range of the list
            return False
        else:
            if i < 0:
                # sets negative i at the right index with the understanding that get() with the
                # same negative index or its corresponding positive index will give the same result
                i = (self.size + i) + 1
            newNode = DLNode(x)
            if self.size == 0:
                self.dummy.front = newNode
                self.dummy.back = newNode
                newNode.back = self.dummy
                newNode.front = self.dummy
            elif i == self.size:
                prevNode = self.get_node(i-1)
                prevNode.front = newNode
                newNode.back = prevNode
                newNode.front = self.dummy
                self.dummy.back = newNode
            else:
                prevNode = self.get_node(i)
                prevNode.back.front = newNode
                newNode.back = prevNode.back
                newNode.front = prevNode
                prevNode.back = newNode
            self.size += 1
            return True

    def remove(self, i):
        '''DL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returs None if i \notin {-n, ... , n-1}.

        Runs in O(1 + min(i, n-i)) time.
        '''
        if i > self.size or i < -1 * (self.size) or self.size == 0:
            return
        else:
            removeNode = self.get_node(i)
            removeNode.back.front = removeNode.front
            removeNode.front.back = removeNode.back
            self.size -= 1
            return removeNode.data

    '''The next few methods involve performing manipulations on
    DLLists. You should complete them without allocating any new nodes
    or temporary arrays. They can all be done only by changing the
    value of front and back in existing nodes.
    '''
    
    def is_palindrome(self):
        '''As described in Exercise 3.7.
        '''
        frontTracker = self.dummy.front
        backTracker = self.dummy.back
        if self.size == 0:
            return True
        else:
            for i in range(int(self.size/2)):
                if frontTracker.data != backTracker.data:
                    return False
                else:
                    frontTracker = frontTracker.front
                    backTracker = backTracker.back
            return True
    
    def truncate(self,i):
        '''As described in Exercise 3.9.
        '''
        if i > self.size or i < -1 * (self.size) or i == self.size: #returns nothing is truncate is done at the end of list
            return
        else:
            newList = DLList()
            currentNode = self.get_node(i)
            newList.dummy.front = currentNode
            self.dummy.back.front = newList.dummy
            self.dummy.back = currentNode.back
            currentNode.back = newList.dummy
            return newList

    def absorb(self,dllist2):
        '''As described in Exercise 3.10.

        Your code should run in O(1) time.
        '''
        if self.size == 0 or dllist2.size == 0:
            return
        else:
            self.dummy.back.front = dllist2.dummy.front
            dllist2.dummy.front.back = self.dummy.back
            dllist2.dummy.back.front = self.dummy
            self.dummy.back = dllist2.dummy.back
            self.size += dllist2.size
    
    def reverse(self):
        '''As described in Exercise 3.12.

        Your code should run in O(n) time.
        '''
        if self.size <= 1:
            return
        else:
            currentNode = self.dummy.back
            while currentNode != self.dummy:
                prevNode = currentNode.back
                currentNode.back = currentNode.front
                currentNode.front = prevNode
                currentNode = prevNode
            temp = self.dummy.front                 #fixing dummy in place
            self.dummy.front = self.dummy.back
            self.dummy.back = temp