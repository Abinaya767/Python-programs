#1
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.sal=int(input("Enter thr salary:"))
    def displayInfo(self):
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()

#2
class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID")
        self.name=input("Enter the name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary:"))
    def displayInfo(self):
        self.displayEmployee()
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()
