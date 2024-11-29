#1  
class Person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name= ",self.name)
class Student(Person):
    def __init__(self,name,studentid):
        super().__init__(name)
        self.studentid=studentid
    def show_student_id(self):
        self.show_name()
        print("student_Id= ",self.studentid)
obj=Student("YYY","abc123")
obj.show_student_id()
