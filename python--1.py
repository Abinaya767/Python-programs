#1
class Students:
    def __init__(self,name,rollnum,mark1,mark2,mark3,mark4,mark5):
        self.name=name
        self.rollnum=rollnum
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.mark4=mark4
        self.mark5=mark5
    def show(self):
        total=self.mark1+self.mark2+self.mark3+self.mark4+self.mark5
        perc=(total/500)*100
        if perc>=85:
            print("Your grade is-->S")
        elif perc>=75:
            print("Your grade is-->A")
        elif perc>=65:
            print("Your grade is-->B")
        elif perc>=55:
            print("Your grade is-->C")
        else:
            print("Yourgrade is-->D")
name=input("Enter student's name--")
rollnum=input("Enter Rollnumber--")
mark1=int(input("Enter subject 1 mark--"))
mark2=int(input("Enter subject 2 mark--"))
mark3=int(input("Enter subject 3 mark--"))
mark4=int(input("Enter subject 4 mark--"))
mark5=int(input("Enter subject 5 mark--"))
obj=Students(name,rollnum,mark1,mark2,mark3,mark4,mark5)
obj.show()
        
