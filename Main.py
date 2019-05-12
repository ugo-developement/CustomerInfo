import CustomerInfo;
import defusedxml;
import ExSheetFunctions;
import NodeDef;
import numpy;
import sys;
import xlrd;
import xlwt;

from CustomerInfo import *;

from defusedxml.common import EntitiesForbidden
from xlrd import open_workbook

defusedxml.defuse_stdlib()


# Joey Hendrich
# May 11, 2019
# Version: 0.1.0



def main():
    x = Customer_Info('Joey', 'x@x.com')
    x.add_account(New_Account('x@xx.com', 'Active'))
    print(x.accounts[0].email)

#Run Main 

if __name__ == "__main__":
    main();

