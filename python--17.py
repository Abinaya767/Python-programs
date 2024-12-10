class Book:
    def __init__(self,bname,bnum):
        self.bname=bname
        self.bnum=bnum
    def displayBookinfo(self):
        print("Book Name--",self.bname)
        print("Book Number--",self.bnum)
class Author:
    def __init__(self,aut_name):
        self.aut_name=aut_name
    def displayAuthorinfo(self):
        print("Author Name--",self.aut_name)
class Details(Book,Author):
    def __init__(self,bname,bnum,aut_name):
        Book.__init__(self,bname,bnum)
        Author.__init__(self,aut_name)
    def DisplayBookdetails(self):
        print("Book details-->")
        self.displayBookinfo()
        self.displayAuthorinfo()
a=input("enter book name")
b=int(input("enter book number"))
c=input("enter author name")
obj=Details(a,b,c)
obj.DisplayBookdetails()
