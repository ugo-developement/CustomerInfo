# Define Node object for linked lists

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def end_node(self):
        node = self
        while node != None:
            node = node.next

# Print out Linked List

def listprint(list):
    printval = list.headval
