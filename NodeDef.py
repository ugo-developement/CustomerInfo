# Define Node object for linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def end_node(self):
        node = self
        while node != None:
            node = node.next

class SLinkedList:
    def __init__(self):
        self.head = None

    def alphaInsert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        
        else:
            current = self.head
            while current is not None and current.next is not None and current.next.data.name < new_node.data.name:
                current = current.next
            new_node.next = current.next
            current.next = new_node

