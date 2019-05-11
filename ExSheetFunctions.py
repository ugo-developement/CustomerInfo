import defusedxml;
import numpy;
import xlrd;
import xlwt;


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


def get_new_users(file):
    var = file;

