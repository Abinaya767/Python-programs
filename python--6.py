#2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print("Name of the Employee=",self.name)
        print("Salary= ",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,depart_name):
        super().__init__(name,salary)
        self.depart_name=depart_name
    def  display_department(self):
        self.display_details()
        print("Department Name= ",self.depart_name)
obj=Manager("YYYY","40k","Computer Science")
obj.display_department()
