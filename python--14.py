class Student:
    def __init__(self,name,age,rollno,s1,s2,s3):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def display(self):
       print("student name--",self.name)
       print("student age--",self.age)
       print("student rollno--",self.rollno)
       print("Subject 1 mark--",self.s1)
       print("Subject 2 mark--",self.s2)
       print("Subject 3 mark--",self.s3)
class Details(Student):
    def __init__(self,name,age,rollno,s1,s2,s3):
        Student.__init__(self,name,age,rollno,s1,s2,s3)
    def show(self):
        total=self.s1+self.s2+self.s3
        per=(total/300)*100
        print("Student Percentage=",per)
obj=Details("yyy","17","e24ai001",97,86,90)
obj.display()
obj.show()
    
