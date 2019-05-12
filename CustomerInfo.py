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
        
        # Any suspected duplicate accounts
        self.accounts = []

        # General user stats and information
        self.info = None

    def set_order_head(self, orders_head):
        self.orders = orders_head

    def add_account(self, new_account):
        self.accounts.append(new_account)

    def set_info(self, new_info):
        self.info = new_info


# Objects for Customer_Info

class New_Order:
    def __init__(self, price, basket):
        self.price = price
        self.basket = basket

class New_Account:
    def __init__(self, email, status):
        self.email = email

        #Is the alleged duplicate "Active" or "Inactive"
        self.status = status

class New_Info:
    def __init__(self, bCount, pCount, bSum, pSum, largestBasket, smallestBasket,
    largestPrice, smallestPrice):
        #self.ip = ip
        self.bCount = bCount
        self.pCount = pCount
        self.bSum = bSum;
        self.pSum = pSum
        self.avgBasket = None
        self.largestBasket = largestBasket
        self.smallestBasket = smallestBasket
        self.avgPrice = None
        self.largestPrice = largestPrice
        self.smallestPrice = smallestPrice


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



