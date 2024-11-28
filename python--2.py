#2
class Student:
    def __init__(self,name,age,course,grade):
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def toshow(self):
        print("Student Name--",self.name)
        print("Student Age--",self.age)
        print("Student Course--",self.course)
        print("Student Grade--",self.grade)
    def __del__(self):
        print("All the details are deleted..!")
name=input("Enter Name= ")
age=int(input("Enter Age= "))
course=input("Enter Course= ")
grade=input("Enter Grade= ")
obj=Student(name,age,course,grade)
obj.toshow()
del obj
