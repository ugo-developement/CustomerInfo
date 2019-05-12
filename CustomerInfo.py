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

class Customer_Info:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        # List of any orders made from this account
        self.orders = None
        
        # Total accounts user might have initialized at 1 for current account
        #self.accounts = 1

        # General user stats and information
        self.info = None

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_order(self, orders_head):
        self.orders = orders_head

    def set_info(self, new_info):
        self.info = new_info

    def set_role(self, new_role):
        self.info.role = new_role

    def update(self, status, lo, bs, ps):
        if self.info is None:
            self.info = New_Info()
        else:
            self.info.status = status
            self.info.ordersTotal = self.info.ordersTotal + 1
            self.info.lastOrder = lo
            self.info.baskSum = self.info.baskSum + bs
            self.info.priceSum = self.info.priceSum + ps
            self.info.avgBasket = float(self.info.baskSum) / float(self.info.ordersTotal)
            self.info.avgPrice = float(self.info.priceSum) / float(self.info.ordersTotal)


# Objects for Customer_Info

class New_Order:
    def __init__(self, price, basket):
        if price is '#######':
            self.price = 0
        else:
            self.price = price
        self.basket = basket

    def set_status(self, new_status):
        self.status = new_status

class New_Info:
    def __init__(self):
        self.status = None
        self.role = 'New'
        self.ordersTotal = 0
        self.lastOrder = None
        self.baskSum = 0
        self.avgBasket = 0
        self.priceSum = 0
        self.avgPrice = 0

    def update(self, status, lo, bs, ps):
        self.status = status
        self.ordersTotal = self.ordersTotal + 1
        self.lastOrder = lo
        self.baskSum = self.baskSum + bs
        self.priceSum = self.priceSum + ps
        self.avgBasket = float(self.baskSum) / float(ordersTotal)
        self.avgPrice = float(self.priceSum) / float(ordersTotal)


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



