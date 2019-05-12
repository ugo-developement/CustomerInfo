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
    user_LL = SLinkedList()

    file = secure_open_workbook(sys.argv[1])
    sheet = file.sheet_by_index(1)
    new_wb = Workbook()
    results = new_wb.add_sheet('Results')

    prev_year = []
    curr_year = []
    known_users = []
    dup = 0

    sheet = file.sheet_by_index(1)
    x = 1
    while x < file.nsheets:
        sheet = file.sheet_by_index(x)

        # User Portion
        y = 1
        while y < sheet.nrows:
            new_user = get_new_user(sheet, y)
            print(new_user.name)
            if [new_user.name.lower(), new_user.email.lower()] not in known_users:
                known_users.append([new_user.name.lower(), new_user.email.lower()])
                update_user_info(sheet, y, new_user, new_user.name.lower(), new_user.email.lower(), user_LL, 'make')
                user_LL.alphaInsert(Node(new_user))
            else:
                print('UPDATE CALLED')
                print("Trying to update: {} {}".format(new_user.name, new_user.email))
                update_user_info(sheet, y, new_user, new_user.name.lower(), new_user.email.lower(), user_LL, 'update')
            curr_year.append([new_user.name.lower(), new_user.email.lower()])
            y = y + 1


        det_users_role(user_LL, prev_year)
        role_count = count_roles(user_LL) # list [new, repeat, loyal, lost, dup]
        data = get_ugo_info(sheet)
        prep_results(results, sheet.name, x)
        write_ugo_info(results, data, x, role_count)

        prev_year = curr_year
        curr_year = []
        print('ON TO NEXT SHEET')
        x = x + 1

    user_results = new_wb.add_sheet('User Results')
    us_head = user_LL.head
    user_results.write(0, 0, 'Customer Name')
    user_results.write(0, 2, 'Customer Email')
    user_results.write(0, 4, 'Avg Basket Size')
    user_results.write(0, 5, 'Avg Price')
    user_results.write(0, 6, 'Account Status')
    dex_row = 1
    while dex_row <= get_LL_len(user_LL):
        user_results.write(dex_row, 0, us_head.data.name)
        user_results.write(dex_row, 2, us_head.data.email)
        user_results.write(dex_row, 4, round(us_head.data.info.avgBasket, 2))
        user_results.write(dex_row, 5, round(us_head.data.info.avgPrice, 2))
        user_results.write(dex_row, 6, us_head.data.info.role)
        us_head = us_head.next
        dex_row = dex_row + 1

    new_wb.save('results.xls')

# Run Main 
if __name__ == "__main__":
    main()