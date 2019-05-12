import CustomerInfo;
import numpy;
import xlrd;
import xlwt;

from CustomerInfo import *
from NodeDef import *

def new_LL(new_node):
    new_LL = SLinkedList()
    new_LL.head = Node(new_node)
    return new_LL

def user_node_by_name(name, head):
    new_head = head
    while new_head.data.name is not name and new_head.next is not None:
        new_head = new_head.next
    if head.data.name is name:
        return new_head
    else:
        return None


