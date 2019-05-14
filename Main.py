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

def rmain():
    # file path, surrounded in r"" for 
    # the sake of spaces
    path = r"{}".format(sys.argv[1])
    print(path)

    # core total users linked list
    user_LL = SLinkedList()

    # open excel file securely
    file = secure_open_workbook(path)

    # set focus on second sheet in file
    sheet = file.sheet_by_index(1)

    # create results file
    new_wb = Workbook()

    # add results sheet and user_results sheet to excel file
    results = new_wb.add_sheet('Results')
    user_results = new_wb.add_sheet('User Results')

    # list containing users from previous year
    prev_year = []

    # temp list containing users found in current year
    curr_year = []

    # list containing all recorded users. likely a waste of memory and processing power
    # but it speeds up checking for existing users as linked lists can only be searched
    # linearly while lists can be searched simply with 'if [name, email] in known_users'
    known_users = []

    # duplicate account count holder. plan on removing
    dup = 0

    # simple counter
    x = 1

    # while x is less than the number of sheets in the excell file do:
    while x < file.nsheets:

        # set focused sheet based on counter x. increases when while loop 
        # ends meaning that all info from that sheet has been extracted
        sheet = file.sheet_by_index(x)

        # User Portion of the data collection begins here...

        # simple counter to keep track of current row
        y = 1

        # while there are rows to get data from do...
        while y < sheet.nrows:

            # create new user object. this needs to be moved. 
            # extremely inefficient for memory.
            # should only create a new_user when program knows
            # that an object for this user doesn't already exist.
            new_user = get_new_user(sheet, y)

            # simple print for debugging purposes
            print(new_user.name)

            # if user is not in known_users list do...
            ### this is where I should create the new_user object. ###
            if [new_user.name.lower(), new_user.email.lower()] not in known_users:

                # 1.) add simple object containing user name and email to known_users list
                # 2.) 'make' the new user's info attribute. info is it's own seperate class
                #     as it has many attributes so we store the info objects as an attribute
                #     to the user.
                # 3.) finally, alphabetically insert the new user into the user_LL (user linked list) 
                known_users.append([new_user.name.lower(), new_user.email.lower()])
                update_user_info(sheet, y, new_user, new_user.name.lower(), new_user.email.lower(), user_LL, 'make')
                user_LL.alphaInsert(Node(new_user))

            else:
                # if the user already exists, call update_user_info with type 'update' so that it knows
                # to find the existing user in the user_LL and then update their info attribute
                print('UPDATE CALLED')
                print("Trying to update: {} {}".format(new_user.name, new_user.email))
                update_user_info(sheet, y, new_user, new_user.name.lower(), new_user.email.lower(), user_LL, 'update')

            # always add the user, new or existing, to the list of current year users
            # so that we can easily keep up with previous years
            curr_year.append([new_user.name.lower(), new_user.email.lower()])

            # move on to the next row
            y = y + 1

        # 1.) using the user linked list and previous year list, update
        #     users' roles (repeat, loyal, lost)
        # 2.) count and add up all the roles of users in user_LL for Ugo Info
        # 3.) data - takes in current sheet and then collects user
        #     basket and price information before returning object
        #     of type Ugo_Info
        # 4.) preps results sheet page (writes column names etc.)
        det_users_role(user_LL, prev_year)
        role_count = count_roles(user_LL) # list [new, repeat, loyal, lost, dup]
        data = get_ugo_info(sheet)
        prep_results(results, sheet.name, x)
        write_ugo_info(results, data, x, role_count)

        # update previous year, clear current year, move on to next sheet
        prev_year = curr_year
        curr_year = []
        print('ON TO NEXT SHEET')
        x = x + 1

    # write individual users' info to user_results sheet
    index = 1
    write_user_info(user_results, user_LL, index)

    # save workbook to current directory
    new_wb.save('results.xls')

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
            new_wb.save('RandC_Results.xls')
            print("Success!")
            break
                








# Run Main 
if __name__ == "__main__":
    main()