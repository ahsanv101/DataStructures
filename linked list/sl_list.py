class SLNode:
    def __init__(self, data):
        self.data = data
        self.front = None  

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''

        return str(self.data)


class SLList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        '''Returns a string representation of an object for printing.
        '''
        lst = ""
        if self.head != None:
            CurrNode = self.head
            for i in range(self.size):
                if (i == self.size-1):
                    lst=lst + str(CurrNode)
                else:
                    lst=lst + str(CurrNode) + ','
                CurrNode=CurrNode.front
        return lst

    def get(self, i):
        '''SL.get(int) -> value

        Returns the value stored at index, i.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''

        if (i > self.size or i == self.size):
            return None
        else:
            tNode = self.head
            for j in range(self.size):
                if j == i:
                    return tNode.data
                else:
                    tNode = tNode.front


    def set(self, i, x):
        '''SL.set(int, value) -> bool

        Sets the element at index, i, to x and returns True.
        Returns False if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''

        if (i >= self.size):
            return False
        else:
            tNode = self.head
            for j in range(self.size):
                if j == i:
                    tNode.data = x
                    return True
                else:
                    tNode = tNode.front



    def add(self, i, x):
        '''SL.add(int, value) -> bool

        Inserts x at index, i, and returns True.
        Returns False if i \notin {0, ..., n}.

        Runs in O(1+i) time.
        '''

        if i <0 or i > self.size:
            return False
        else:
            nNode = SLNode(x)
            if self.size == 0:
                self.head = nNode
                self.size+=1
                return True
            else:
                n = 0
                tNode = self.head
                if i == 0:
                    self.head = nNode
                    nNode.front = tNode
                    self.size+=1
                    return True
                else:
                    while n < self.size:
                        if (n == i-1):
                            tNextNode = tNode.front
                            tNode.front = nNode
                            nNode.front = tNextNode

                            if (n == self.size-1):
                                self.tail = nNode
                            self.size += 1
                            return True
                        else:
                            tNode = tNode.front
                        n+=1



    def remove(self, i):
        '''SL.remove(int) -> value

        Removes the element at index, i, and returns it.
        Returns None if i \notin {0, ..., n-1}.

        Runs in O(1+i) time.
        '''

        if (i >self.size or i  == self.size):
            return False
        else:
            tNode = self.head
            if i == 0:
                self.head = self.head.front
                self.size-=1
                return tNode.data
            else:
                for j in range(self.size):
                    if (j == i-1):
                        val = tNode.front
                        tNode.front = tNode.front.front
                        self.size-=1
                        if j == self.size-1:
                            self.tail = tNode
                        return val.data
                    else:
                        tNode = tNode.front
        

