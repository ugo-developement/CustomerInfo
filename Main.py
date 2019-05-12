import CustomerInfo;
import defusedxml;
import ExSheetFunctions;
import LinkedListFunctions;
import NodeDef;
import numpy;
import sys;
import xlrd;
import xlwt;

from CustomerInfo import *
from ExSheetFunctions import *
from LinkedListFunctions import *

from defusedxml.common import EntitiesForbidden
from xlrd import open_workbook
from xlwt import Workbook

defusedxml.defuse_stdlib()


# Joey Hendrich
# May 11, 2019
# Version: 0.1.0



def main():
    customer1 = Customer_Info('joey', 'joey@xxx.com')
    customer2 = Customer_Info('kewl', 'kewl@xxx.com')

    user_LL = SLinkedList()
    user_LL.head = Node(customer1)
    print(user_LL.head.data.name)
    user_LL.alphaInsert(Node(customer2))
    print(user_LL.head.next.data.name)

    #file = secure_open_workbook(sys.argv[1])
    #new_wb = Workbook()
    #results = new_wb.add_sheet('Results')
    #i = 1
    #while i < file.nsheets:
    #    sheet = file.sheet_by_index(i)
    #    data = get_ugo_info(sheet)
    #    prep_results(results, sheet.name, i)
    #    write_ugo_info(results, data, i)
    #    i = i + 1

    #new_wb.save('results.xls')

# Run Main 
if __name__ == "__main__":
    main()