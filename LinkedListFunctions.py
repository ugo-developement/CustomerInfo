import CustomerInfo;
import NodeDef;
import numpy;

from CustomerInfo import *
from NodeDef import *

def new_LL(new_node):
    new_LL = SLinkedList()
    new_LL.head = Node(new_node)
    return new_LL

def get_LL_len(inll):
    i = 0
    head = inll.head
    while head is not None:
        i = i + 1
        head = head.next
    return i

def user_node_by_name(name, head):
    new_head = head
    while new_head.data.name is not name and new_head.next is not None:
        new_head = new_head.next
    if head.data.name is name:
        return new_head
    else:
        return None

# Set up 'lost' role
def det_users_role(userll, prev_year):
    head = userll.head
    while head is not None:
        if [head.data.name, head.data.email] in prev_year:
            if head.data.info.role == 'new':
                head.data.set_role('repeat')
            elif head.data.info.role == 'repeat':
                head.data.set_role('loyal')
        head = head.next

def count_roles(userll):
    list = [0, 0, 0, 'Not Done', 'Not Done']
    head = userll.head
    while head is not None:
        if head.data.info.role == 'new':
            list[0] = list[0] + 1
        elif head.data.info.role == 'repeat':
            list[1] = list[1] + 1
        elif head.data.info.role == 'loyal':
            list[2] = list[2] + 1
        head = head.next
    return list