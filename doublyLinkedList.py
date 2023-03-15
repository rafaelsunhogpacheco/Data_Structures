# Linked List

class Node:
    def __init__(self):
        self._data = None
        self._nextNode = None
        self._prevNode = None
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def newValue(self,newData):
        self._data = newData
    
    @property
    def nextNode(self):
        return self._nextNode
    
    @nextNode.setter
    def newNextNode(self,newNextNode):
        self._nextNode = newNextNode

    @property
    def prevNode(self):
        return self._prevNode
    
    @prevNode.setter
    def newPrevNode(self,newPrevNode):
        self._prevNode = newPrevNode


class dl_List:
    def __init__(self):
        self._head = None
        self._tale = None
        self._size = 0
    
    # Insert Element at the beggining
    def addHead(self,data):
        newNode = Node(data)

        if newNode == None:
            return False
        
        # Insert Element to Empty list
        if self.head == None:
            self.head = newNode
            self.tale = newNode
        else:
            self.head.prevNode = newNode
            self.head = newNode
        self._size += 1
    
    # Insert Element at the end
    def addTale(self,data):
        # Check if the list is empty
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
            self.tale = newNode
        #Iterate untill next == None
        else:
            n = self.head
            while n.nextNode != None:
                n = n.nextNode
            newNode = Node(data)
            n.nextNode = newNode
            newNode.prevNode = n
        self._size += 1
    
    # Remove Element at the beggining
    def removeHead(self):
        if self.head == None:
            return False
        if self.head.newNextNode == None:
            self.head = None
            return
        self.head = self.head.nextNode
        self.head.prevNode = None




