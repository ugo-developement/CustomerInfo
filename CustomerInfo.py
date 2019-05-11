import sys;


# Customer_Info Class Definition
# Stores Customer Specific Info

# Orders:
# Points to head of linked list consisting of all known orders
# 

class Customer_Info:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = None
        self.accounts = None
        self.info = None

    def add_order_LinkedList(self, order_head):
        self.orders = order_head

    def add_account_LinkedList(self, account_head):
        self.account = account_head

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
        self.status = status #Is the alleged duplicate "Active" or "Inactive"

class New_Info:
    def __init__(self, ip, bCount, pCount, avgBasket, largestBasket, smallestBasket,
    avgPrice, largestPrice, smallestPrice):
        self.ip = ip
        self.bCount = bCount
        self.pCount = pCount
        self.avgBasket = avgBasket
        self.largestBasket = largestBasket
        self.smallestBasket = smallestBasket
        self.avgPrice = avgPrice
        self.largestPrice = largestPrice
        self.smallestPrice = smallestPrice

