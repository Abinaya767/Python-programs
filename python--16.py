class Student:
    def __init__(self,name,age,dep,rollno):
        self.name=name
        self.age=age
        self.dep=dep
        self.rollno=rollno
    def studentinfo(self):
        print("Student Name=",self.name)
        print("Student Age=",self.age)
        print("Student Department=",self.dep)
        print("Student Roll Number=",self.rollno)
class StudentAthelete(Student):
    def __init__(self,name,age,dep,rollno,sport):
        super().__init__(name,age,dep,rollno)
        self.sport=sport
    def displayAtheleteInfo(self):
        self.studentinfo()
        print("Sports Name=",self.sport)
obj=StudentAthelete("Abinaya",17,"AI","E24AI001","Cricket")
obj.displayAtheleteInfo()
