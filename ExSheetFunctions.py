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
from xlwt import XFStyle

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

#
# Function: Get data about Ugo
# Return: Ugo_Info object
# Usage: Collect out put data
# about Ugo for individual years
#

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

#
# Function: Create a new user object
# Return: Customer_Info object
# Usage: Create new users to be stored
# inside of the User Linked List
#

def get_new_user(file, row):
    user = Customer_Info(file.cell_value(row, 0).lower(), file.cell_value(row, 1).lower())
    return user


#
# Funtion: Find user in workbook sheet
# Return: True or False
# Usage: Check activity of account that year
#

def get_active_bool(sheet, user): #(wb sheet, user_ll.head.data)
    name = user.name
    email = user.email

    i = 1
    while i < sheet.nrows:
        if name is sheet.cell_value(i, 0) and email is sheet.cell_value(i, 1):
            return True
    return False


#
# Function: Update specific user's info
# Usage: Update user info
#

def update_user_info(file, row, user, userN, userE, userll, type):
    dog = row



##########################################
#                                        #
###### XLWT (Excel Write) Functions ######
#                                        #
##########################################

#
# Function: Prepare 'Results' sheet
# Usage: Write column descriptions
# and data desctiptions to 'Results'
#

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
        file.write(index, 4, round(us_head.data.info.baskAvget, 2))
        file.write(index, 5, round(us_head.data.info.priceAvg, 2))
        file.write(index, 6, us_head.data.info.role)
        us_head = us_head.next
        index = index + 1


#
# Function: Write user linked list to sheet
# for debugging purposes
# Usage: Debugging
#

def debug_write_LL(sheet, llist):
    format_dates = XFStyle()
    format_dates.num_format_str = 'M/D/YY'
    head = llist.head
    row = 0
    while head is not None:
        sheet.write(row, 0, head.data.name)
        sheet.write(row, 1, head.data.email)
        sheet.write(row, 2, head.data.info.created, format_dates)
        sheet.write(row, 3, 'Dups: {}'.format(len(head.data.accounts)))

        if len(head.data.accounts) > 0:
            i = 0
            for x in head.data.accounts:
                sheet.col(4 + i).width = 256 * 30
                sheet.write(row, 4 + i, head.data.accounts[i])
                i += 1
        print(head.data.name)
        head = head.next
        row += 1