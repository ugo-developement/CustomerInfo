import CustomerInfo;
import defusedxml;
import ExSheetFunctions;
import NodeDef;
import numpy;
import sys;
import xlrd;
import xlwt;

from CustomerInfo import *
from ExSheetFunctions import *

from defusedxml.common import EntitiesForbidden
from xlrd import open_workbook
from xlwt import Workbook

defusedxml.defuse_stdlib()


# Joey Hendrich
# May 11, 2019
# Version: 0.1.0



def main():
    

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