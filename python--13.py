class School:
    def __init__(self,scl_name):
        self.scl_name=scl_name
    def show(self):
        print("School Name--",self.scl_name)
class Student(School):
    def __init__ (self,stu_name):
        self.stu_name=stu_name
    def disp(self):
        print("Student Name--",self.stu_name)
class Details(School):
    def __init__(self,stu_age):
        self.stu_age=stu_age
    def displayDet(self):
        print("Student Age--",self.stu_age)
class Info1(Student,Details):
    def __init__(self,scl_name,stu_name,stu_age):
        School.__init__(self,scl_name)
        Student.__init__(self,stu_name)
        Details.__init__(self,stu_age)
    def Toshow1(self):
        print("Details1---")
        self.show()
        self.disp()
        self.displayDet()
obj1=Info1("YYY","XXX",17)
obj1.Toshow1()
