import CustomerInfo;
import defusedxml;
import LinkedListFunctions;
import NodeDef;
import numpy;
import xlrd;
import xlwt;

from CustomerInfo import *
from LinkedListFunctions import *
from NodeDef import *

from defusedxml.common import EntitiesForbidden;
from xlrd import open_workbook;

defusedxml.defuse_stdlib();




##################################
#                                #
##### Defused XML Functions ######
#                                #
##################################

# Protection against XML related attacks
# XML attacks can (and will):
# Expose critical info, crash server, lock up server,
# literally destroy the server, and finally, 
# they will fuck our shit up. Don't touch.


def secure_open_workbook(xfile):
    try:
        return open_workbook(xfile);
    except EntitiesForbidden:
        raise ValueError('Please only use xlsx files without XEE');




##########################################
#                                        #
###### XLRD (Excel Read) Functions #######
#                                        #
##########################################

# Read data from excel sheets


def get_ugo_info(file):
    data = Ugo_Info(0, 0, 1, 1)
    indexRow = 1
    while indexRow < file.nrows:
        data.add_to_bSum(file.cell_value(indexRow,3))
        if file.cell_value(indexRow, 3) > data.bLarge:
            data.set_bLarge(file.cell_value(indexRow, 3))
        if file.cell_value(indexRow, 3) < data.bSmall:
            data.set_bSmall(file.cell_value(indexRow, 3))
        indexRow = indexRow + 1

    return data

def get_new_user(file, row):
    user = Customer_Info(file.cell_value(row, 0).lower(), file.cell_value(row, 1).lower())
    return user

def update_user_info(file, row, user, userN, userE, userll, type):
    # Python u wild lol
    if type is 'update':
        

        #order = New_Order(file.cell_value(row, 5), file.cell_value(row, 4))

        head = userll.head
        if head is not None:
            if head.data.name.lower() == userN and head.data.email.lower() == userE:
                dog = head
                #head.data.orders.pushInsert(Node(order))

            else:
                while head is not None:
                    if head.data.name.lower() == userN and head.data.email.lower() == userE:
                        print('User found. Updating')
                        break
                    head = head.next
                #head.data.orders.pushInsert(Node(order))
                #head.data.update('Active', head.data.orders.head, order.basket, order.price)

    else:
        #order_ll = SLinkedList()
        #order = New_Order(file.cell_value(row, 5), file.cell_value(row, 4))
        #order_ll.pushInsert(Node(order))
        #user.set_order(order_ll)

        info = New_Info()
        info.status = 'Active'
        info.role = 'new'
        info.ordersTotal = 1
        #info.lastOrder = user.orders.head
        #info.baskSum = info.baskSum + order.basket
        #info.priceSum = info.priceSum + order.price
        info.avgBasket = float(info.baskSum) / float(info.ordersTotal)
        info.avgPrice = float(info.priceSum) / float(info.ordersTotal)
        user.set_info(info)



##########################################
#                                        #
###### XLWT (Excel Write) Functions ######
#                                        #
##########################################

# Write to excel sheets
def prep_results(file, sheet, index):
    indexF = index * 10
    file.write(0 + indexF, 0, 'RESULTS FOR ' + sheet)
    file.write(0 + indexF, 3, 'Ugo Data') # Data info written to col 3, values to col 5
    file.write(1 + indexF, 3, 'Total Orders')
    file.write(2 + indexF, 3, 'Avg Basket Size')
    file.write(3 + indexF, 3, 'Largest Basket') 
    file.write(4 + indexF, 3, 'Smallest Basket')

    file.write(0 + indexF, 7, 'Customer Data (Skewed due to duplicates, working on fix)')
    file.write(1 + indexF, 7, 'New')
    file.write(2 + indexF, 7, 'Repeat')
    file.write(3 + indexF, 7, 'Loyal')
    file.write(4 + indexF, 7, 'Lost')
    file.write(5 + indexF, 7, 'Duplicate')

def write_ugo_info(file, data, index, roles):
    indexF = index * 10
    file.write(1 + indexF, 5, data.bCount)
    file.write(2 + indexF, 5, round(data.bAvg, 2))
    file.write(3 + indexF, 5, data.bLarge)
    file.write(4 + indexF, 5, data.bSmall)

    file.write(1 + indexF, 8, roles[0])
    file.write(2 + indexF, 8, roles[1])
    file.write(3 + indexF, 8, roles[2])
    file.write(4 + indexF, 8, roles[3])
    file.write(5 + indexF, 8, roles[4])

def write_user_info(file, userll, index):
    us_head = userll.head
    file.write(0, 0, 'Customer Name')
    file.write(0, 2, 'Customer Email')
    file.write(0, 4, 'Avg Basket Size')
    file.write(0, 5, 'Avg Price')
    file.write(0, 6, 'Account Status')
    while index <= get_LL_len(userll):
        file.write(index, 0, us_head.data.name)
        file.write(index, 2, us_head.data.email)
        file.write(index, 4, round(us_head.data.info.avgBasket, 2))
        file.write(index, 5, round(us_head.data.info.avgPrice, 2))
        file.write(index, 6, us_head.data.info.role)
        us_head = us_head.next
        index = index + 1