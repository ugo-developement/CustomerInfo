import sys;


# Could maybe try:
# class Customer_Info:
#   pass
# and create objects like so:
# 

# Customer_Info Class Definition
# Stores Customer Specific Info

# Orders:
# Points to head of linked list consisting of all known orders
# 

# TO DO:
# - Need to store duplicate accounts inside customer objects
# - Need to update the user email, orders (should contain total of active and dups), 
#   and info whenever a duplicate becomes active and main goes inactive


# Rework so Customer Profile works like so:
# Customer
# name
# email
# orders[[year, amount of orders], [year, amount of orders]]
# accounts = [obj.dup_account1, obj.dup_account2]
# info 
# - info.status = 'active' 'duplicate' 'inactive'
# - info.role = 'new' or 'repeat' or 'loyal' or 'lost'
# - info.yrs 
# - info.created = 'mm/dd/yyyy'
# - info.ordTotal 
# - info.baskSum 
# - info.avgBask
# - info.priceSum
# - info.avgPrice
class Customer_Info:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        # List of objects containing year and total orders
        self.orders = []
        
        # List pointing to customer objects of duplicates
        self.accounts = []

        # General user stats and information
        self.info = None

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def add_order(self, order):
        self.orders.append(order)

    def set_info(self, new_info):
        self.info = new_info

    def set_role(self, new_role):
        self.info.role = new_role

    def set_status(self, status):
        self.info.status = status

    # This will ALWAYS increase the user's years with ugo by 1. 
    # Change this mechanic later
    def update(self, status, ot, bs, ps):
        self.info.status = status
        self.info.yrs = self.info.yrs + 1
        self.info.ordTotal = self.info.ordTotal + ot
        self.info.baskSum = self.info.baskSum + bs
        self.info.priceSum = self.info.priceSum + ps
        self.info.avgBasket = float(self.info.baskSum) / float(self.info.ordTotal)
        self.info.avgPrice = float(self.info.priceSum) / float(self.info.ordTotal)


# Info Class for Customer_Info

# On Initialization, must take in:
# Status (Can only be Active or Duplicate when Initializing)
# Created (Year created)
# Everything else defaults to constant values true for all new info classes
class New_Info:
    def __init__(self, status, created):
        self.status = status
        self.role = 'new'
        self.yrs = 1 # years with ugo
        self.created = created
        self.ordTotal = 0
        self.baskSum = 0
        self.avgBasket = 0 # average of x years
        self.priceSum = 0
        self.avgPrice = 0 # average of x years


# Info for Ugo as a whole

class Ugo_Info:
    def __init__(self, bCount, bSum, bLarge, bSmall):
        self.bCount = bCount
        self.bSum = bSum
        self.bLarge = bLarge
        self.bSmall = bSmall
        self.oCount = 0
        self.bAvg = 0

    def set_bLarge(self, size):
        self.bLarge = int(size)

    def set_bSmall(self, size):
        self.bSmall = int(size)

    def add_to_bSum(self, size):
        self.bSum = self.bSum + int(size)
        self.bCount = self.bCount + 1
        self.bAvg = float(self.bSum) / float(self.bCount)



