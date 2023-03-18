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

   

def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data