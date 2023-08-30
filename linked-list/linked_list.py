class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self): 
        cur = self.head
        total = 0
        while cur.next is not None:
            total +=1
            cur = cur.next
        return total

    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next is not None:
              cur_node = cur_node.next
              elem.append(cur_node.data)  
        print(elem)    

    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None    
        cur_index=0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index +=1

    def erase(self, index):
        if index>= self.length():
           print("ERROR: Index out of range")
           return None       
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index==index:
                last_node.next = cur_node.next
                return 
            cur_index+=1



