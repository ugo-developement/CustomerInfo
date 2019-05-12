import CustomerInfo;
import defusedxml;
import numpy;
import xlrd;
import xlwt;

from CustomerInfo import *

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



##########################################
#                                        #
###### XLWT (Excel Write) Functions ######
#                                        #
##########################################

# Write to excel sheets
def prep_results(file, sheet):
    file.write(0,0, 'RESULTS FOR ' + sheet)
    file.write(0, 3, 'Ugo Data') # Data info written to col 3, values to col 5
    file.write(0, 6, 'Customer Data')
    file.write(1, 3, 'Avg Basket Size')
    file.write(2, 3, 'Largest Basket') 
    file.write(3, 3, 'Smallest Basket') 

def write_ugo_info(file, data):
    file.write(1, 5, round(data.bAvg, 2))
    file.write(2, 5, data.bLarge)
    file.write(3, 5, data.bSmall)