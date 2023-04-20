class car:
    def __init__(self, *args):
       if len(args)==0:
        self.brand=''
        self.year =0
        self.model=''
        self.engineSize=0.0
       elif len(args)==1:
        self.brand=args[0]
        self.year =0
        self.model=''
        self.engineSize=0.0
       elif len(args)==2:
        self.brand=args[0]
        self.year =0
        self.model=''
        self.engineSize=0.0
       elif len(args)==3: 
        self.brand=args[0]
        self.year =0
        self.model=''
        self.engineSize=0.0
       elif len(args)==4:
        self.brand=args[0]
        self.year =0
        self.model=''
        self.engineSize=0.0

    def setBrand(self, brand):
        self.brand = brand
    def getBrand(self):
        return self.brand

    def setYear(self, year):
        self.year = year
    def getYear(self):
        return self.year

    def setModel(self, model):
        self.model = model
    def getModel(self):
        return self.model

    def setengineSize(self, engineSize):
        self.engineSize = engineSize
    def getengineSize(self):
        return self.engineSize


if __name__ == '__main__':
    car = car()
    car.setBrand("toyota")
    car.setYear(-90)
    car.setModel("GodSpeed")
    car.setengineSize(100.5)
    print(car.getBrand())
    print(car.getYear())
    print(car.getModel())
    print(car.getengineSize())
    