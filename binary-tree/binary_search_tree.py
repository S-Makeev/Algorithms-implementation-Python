class Node:
  def __init__(self, data=None):
    self.data = data
    self.left_child = None
    self.right_child = None

class Binary_Search_Tree:
  def __init__(self):
    self.root = None

  def insert(self, data):
      if self.root is None:
          self.root = Node(data)
      else:
         self._insert()    