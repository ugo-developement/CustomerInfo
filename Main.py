import CustomerInfo;
import defusedxml;
import ExSheetFunctions;
import NodeDef;
import numpy;
import sys;
import xlrd;
import xlwt;

from CustomerInfo import *;
from ExSheetFunctions import *;

from defusedxml.common import EntitiesForbidden
from xlrd import open_workbook
from xlwt import Workbook

defusedxml.defuse_stdlib()


# Joey Hendrich
# May 11, 2019
# Version: 0.1.0



def main():
    file = secure_open_workbook(sys.argv[1])
    sheet = file.sheet_by_index(1) # 2015 sheet
    data = get_ugo_info(sheet)

    new_wb = Workbook()
    results = new_wb.add_sheet('Results')
    prep_results(results, sheet.name)
    write_ugo_info(results, data)

    new_wb.save('results.xls')

# Run Main 
if __name__ == "__main__":
    main()

