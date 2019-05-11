import defusedxml;
import ExSheetFunctions;
import numpy;
import sys;
import xlrd;
import xlwt;

from defusedxml.common import EntitiesForbidden;
from xlrd import open_workbook;

defusedxml.defuse_stdlib();


# Joey Hendrich
# May 11, 2019
# Version: 0.1.0



##################################
#                                #
###### Begin Code for Main #######
#                                #
##################################

def main():
    argv = sys.argv;
    
    for x in range (1, len(argv)):
        print("Hello World!");






#Run Main 

if __name__ == "__main__":
    main();

