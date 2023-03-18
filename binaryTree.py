# Binary Tree

class Node:
   def __init__(self, data):
      self.data = data
      self.right = None
      self.left = None
   
   @property
   def data(self):
      return self.data
   
   def __str__(self):
      return str(self.data)

   
class binaryTree:
   def __init__(self):
      self.root = None
   
   def addNode(self,data):
      node = Node()
      self.data = data

      if self.data == None:
         self.data = node
         return True
      else:
         aux = self.root

         while aux != None:
            if data < aux.data:
               return False
            elif aux.data > data:
               if aux.left != None:
                  aux = aux.left
               else:
                  aux.left = node
                  return True
            else:
               if aux.right != None:
                  aux = aux.right
               else:
                  aux.right = node
                  return True
   def search(self, data):
      aux = self.root
      while self.data != data:
         if self.data < data:
            aux = aux.left
         else:
            aux = aux.right
         if self.data == None:
            return None
      return aux
         

