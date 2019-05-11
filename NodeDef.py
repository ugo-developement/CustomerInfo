# Define Node object for linked lists

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


# Print out Linked List

def listprint(list):
    printval = list.headval
    