# Linked List

class Node:
    def __init__(self,data):
        self._data = data
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
    
    def __str__(self):
        return f"{self.data}"


class dl_List:
    def __init__(self):
        self._head = None
        self._tale = None
        self._size = 0

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, newHead):
        self._head = newHead

    @property
    def tale(self):
        return self._tale

    @tale.setter
    def tale(self, newTale):
        self._tale = newTale

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, newSize):
        self._size = newSize

    
    # Insert Element at the beggining
    def addHead(self,data):
        newNode = Node(data)

        if newNode == None:
            return False
        
        # Insert Element to Empty list
        if self._head is None:
            self.head = newNode
            self.tale = newNode
        else:
            self.head._prevNode = newNode
            newNode._nextNode = self.head
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
            n._nextNode = newNode
            newNode._prevNode = n
        self._size += 1
    
    # Remove Element at the beggining
    def removeHead(self):
        if self.head == None:
            return False
        if self.head.newNextNode == None:
            self.head = None
            self._size -= 1
            return
        self.head = self.head.nextNode
        self.head._prevNode = None
        self._size -= 1
    
    # Remove Elements at the end
    def removeTale(self):
        if self.head == None:
            return False
        else:
            n = self.head
            while n.nextNode != None:
                n = n.nextNode
            n.prevNode._nextNode = None
            n = None
    
    def __str__(self):
        if self._size == 0:
            return "Empty list"
        elif self._size == 1:
            return f"{self.head}"
        else:
            ref = self.head
            group = ""
            while ref.nextNode is not None:
                group += f"{ref}, "
                ref = ref.nextNode
            group += f"{ref}"
            return group




#################################################
# Testing

# lista = dl_List()





# lista.addHead(5)
# print(lista)
# lista.addTale(8)
# lista.addTale(7)
# lista.addHead(1)
# lista.addHead(9)


# lista.removeHead()
# lista.removeTale()



# print(lista)