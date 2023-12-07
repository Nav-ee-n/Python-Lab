class rectangle:
    def datainput(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print("Area : ",self.length*self.breadth)
    def Perimeter(self):
        print("Perimeter : ",2*(self.length+self.breadth))

obj1=rectangle()
obj1.datainput(12,4)
obj1.area()
obj1.Perimeter()
print("\n")
obj2=rectangle()
obj2.datainput(9,1)
obj2.area()
obj2.Perimeter()
print("\n")


