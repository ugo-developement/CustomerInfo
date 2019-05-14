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
# Version: 0.2.0

def main():
    users_LL = SLinkedList()
    path = r"{}".format(sys.argv[1])
    file = secure_open_workbook(path)

    new_wb = Workbook()
    ugo_results = new_wb.add_sheet('Ugo Results')
    user_results = new_wb.add_sheet('User Results')

    # Styling
    user_results.col(0).width = 256 * 30
    user_results.col(1).width = 256 * 30

    role_list = ['New', 'Repeat', 'Loyal', 'Lost']
    prev_year = []
    curr_year = []
    u_names = []
    u_emails = []

    for index in range(file.nsheets + 1):
        sheet = file.sheet_by_index(index)

        # Sheet containing all created accounts with dates, ip, etc
        # This loop will populate users_LL, u_names, and u_emails
        if index == 0:
            i = 1
            while i < sheet.nrows:
                name = sheet.cell_value(i, 0).lower()
                email = sheet.cell_value(i, 1).lower()
                created = sheet.cell_value(i, 3)
                head = users_LL.head
                done = False

                if email not in u_emails:
                    if name not in u_names:
                        u_names.append(name)
                        new_user = Customer_Info(name, email)
                        new_info = New_Info('Active', created)
                        new_user.set_info(new_info)
                        users_LL.alphaInsert(Node(new_user))
                    else:
                        head = users_LL.head
                        while head is not None:
                            if head.data.name == name and head.data.email != email:
                                if email not in head.data.accounts:
                                    head.data.accounts.append(email)
                                    break
                            head = head.next
                u_emails.append(email)
                i += 1
            # End while
            debug_write_LL(user_results, users_LL)
        else:
            # Begin everything after sheet 0
            i = 1
            while i < sheet.nrows:
                head = users_LL.head
                name = sheet.cell_value(i, 0).lower()
                email = sheet.cell_value(i, 1).lower()
                ot = sheet.cell_value(i, 2)
                bs = sheet.cell_value(i, 3)
                ps = sheet.cell_value(i, 4)
                while head is not None:
                    if head.data.name == name:
                        if head.data.email == email:
                            head.data.update()




    new_wb.save('RandC_Results.xls')
    # Closed work book, end of script.
            
                








# Run Main 
if __name__ == "__main__":
    main()