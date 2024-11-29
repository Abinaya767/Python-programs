#2
class Restaurant:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def displayitems(self):
        print("Food Name--",self.name)
        print("Food Cost--",self.cost)
class Delivery:
    def __init__(self,contactnum,drivername):
        self.contactnum=contactnum
        self.drivername=drivername
    def Deliverydetails(self):
        print("Contact Number -- ",self.contactnum)
        print("Driver Name -- ",self.drivername)
class Order(Restaurant,Delivery):
    def __init__(self,name,cost,contactnum,drivername):
        Restaurant.__init__(self,name,cost)
        Delivery.__init__(self,contactnum,drivername)
    def Toshowall(self):
        self.displayitems()
        self.Deliverydetails()
obj=Order("Biriyani",250,1234567890,"YYYY")
obj.Toshowall()
