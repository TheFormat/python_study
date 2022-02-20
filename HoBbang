from enum import IntEnum
import random

class Dough(IntEnum):
    Normal = 0
    SweetPotato = 1
    SweetPumpkin = 2
    
class Filling(IntEnum):
    Redbean = 0
    SweetPotatoMousse = 1
    SweetPumpkinMousse = 2
    ChestNut = 3

class HoBbang:
    def __init__(self, dough : Dough, filling : Filling):
        self.dough : Dough = dough
        self.filling : Filling = filling
        

class HoBbangPackage:
    def __init__(self, num : int):
        self.num : int = num
        self.price : int = self.num * 600
        self.hobbang = []
        for i in range(0, num):
            self.hobbang.append(HoBbang(Dough(random.randrange(0, 3)), Filling(random.randrange(0, 4))))
        for i in self.hobbang:
            self.price += i.dough * 100
            self.price += i.filling * 100
    
    
pkg = HoBbangPackage(5)

for i in pkg.hobbang:
    print(str(i.dough) + "        " + str(i.filling))
print("\n\n이 모든 구성을 단돈 " + str(pkg.price) + "원에\n")
