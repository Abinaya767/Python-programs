class Game:
    def __init__(self,g1,g2):
        self.g1=g1
        self.g2=g2
    def DisplayGame(self):
        print(f"Game1={self.g1}\nGame2={self.g2}")
class Mobile(Game):
    def __init__(self,g1,g2,mob_model):
        super().__init__(g1,g2)
        self.mob_model=mob_model
    def DisplayMobile(self):
        self.DisplayGame()
        print("Mobile Model=",self.mob_model)
class Storage(Mobile):
    def __init__(self,g1,g2,mob_model,capacity1,capacity2):
        super().__init__(g1,g2,mob_model)
        self.capacity1=capacity1
        self.capacity2=capacity2
    def DisplayStorage(self):
        self.DisplayMobile()
        print("Game 1 Capacity=",self.capacity1)
        print("Game 2 Capacity=",self.capacity2)
class Levels(Storage):
    def __init__(self,g1,g2,mob_model,capacity1,capacity2,levels):
        super().__init__(g1,g2,mob_model,capacity1,capacity2)
        self.levels=levels
    def DisplayLevels(self):
        self.DisplayStorage()
        print("Number of Levels=",self.levels)
obj1=Storage("Free Fire","Pubg","Redmi 12G","560mb","600mb")
obj1.DisplayStorage()
obj2=Levels("Diamond Levels")
obj2.DisplayLevels()
