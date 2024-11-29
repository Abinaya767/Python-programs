#1
class Library:
    def __init__(self,bname,bnumber):
        self.bname=bname
        self.bnumber=bnumber
    def DisplayBook(self):
        print(f"BookName-- {self.bname}\nBookNumber-- {self.bnumber}")
class Member:
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id
    def Display(self):
        print(f"Member's Name-- {self.name}\nMember Id-- {self.Id}")
class LibraryManagement(Library,Member):
    def __init__(self,bname,bnumber,name,Id):
        Library.__init__(self,bname,bnumber)
        Member.__init__(self,name,Id)
    def Toshowall(self):
        self.DisplayBook()
        self.Display()
obj=LibraryManagement("Seventeen Oranges",6,"YYY","E24AI001")
obj.Toshowall()
