class Camera:
    def __init__(self,resolution):
        self.resolution=resolution
    def display(self):
        print("Photo's resolution=",self.resolution)
class Phone:
    def __init__(self,number):
        self.number=number
    def show(self):
        print("Phone Number is=",self.number)
class SmartPhone(Camera,Phone):
    def __init__(self,resolution,number,brand,model):
        super().__init__(resolution)
        Phone.__init__(self,number)
        self.brand=brand
        self.model=model
    def Displaydeviceinfo(self):
        self.display()
        self.show()
        print("Phone brand=",self.brand)
        print("Phone model=",self.model)
obj=SmartPhone("200 MP",1234567890,"Samsung","Galaxy S24 Ultra")
obj.Displaydeviceinfo()
