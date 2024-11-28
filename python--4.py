#1
class Inventory:
    def __init__(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID=",self.prodId)
        print("Product Name=",self.prodName)
        print("Product Count=",self.prodCount)
obj=Inventory("A1234","Lakme",4)
obj.display()

#2
class Inventory:
    def __init__(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount
    def display(self):
        print("Product ID=",self.prodId)
        print("Product Name=",self.prodName)
        print("Product Count=",self.prodCount)
class Todisplay(Inventory):
    def getdet(self):
        self.display()
obj=Todisplay("A1234","Lakme",4)
obj.getdet()




