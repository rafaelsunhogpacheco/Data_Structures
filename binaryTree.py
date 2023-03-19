# Binary Tree

class Node:
   def __init__(self):
      self._right = None
      self._left = None
      self._data = None
   
   @property
   def data(self):
      return self._data
   
   def __str__(self):
      return str(self._data)

   
class binaryTree:
   def __init__(self):
      self._root = None
   
   def addNode(self,data):
      node = Node()
      node._data = data

      if self._root == None:
         self._root = node
         return True
      else:
         aux = self._root

         while aux != None:
            if aux._data == data:
               return False
            elif data < aux._data:
               if aux._left != None:
                  aux = aux._left
               else:
                  aux._left = node
                  return True
            else:
               if aux._right != None:
                  aux = aux._right
               else:
                  aux._right = node
                  return True


   def search(self, data):
      aux = self._root
      while self.data != data:
         if self.data < data:
            aux = aux._left
         else:
            aux = aux._right
         if self.data == None:
            return None
      return aux
         

   # Root, left, right
   def preOrder(self, node):
      if Node != None:
         print(node._data)
         self.preOrder(node._left)
         self.preOrder(node._right)

   #Left, root, right
   def order(self, node):
      if node != None:
         self.order(node._left)
         print(node._data)
         self.order(node._right)

   #Left, raight, root
   def posOrder(self,node):
      if Node != Node:
         self.posOrder(node._left)
         self.posOrder(node._right)
         print(node._data)

   def display(self,node,level):
      count = level
      for i in range(count):
            print("--",end="")
        
      print(node.data)

      if node._left != None:
            count += 1
            self.display(node._left,count)
        
      if node._right != None:
            self.display(node._right,count)






arvore = binaryTree()




arvore.addNode(53)
arvore.addNode(30)
arvore.addNode(72)
arvore.addNode(14)
arvore.addNode(39)
arvore.addNode(9)
arvore.addNode(23)
arvore.addNode(34)
arvore.addNode(49)
arvore.addNode(61)
arvore.addNode(84)
arvore.addNode(79)
arvore.display(arvore._root,0)

print('Em ordem:')
arvore.order(arvore._root)