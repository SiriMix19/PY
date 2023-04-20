class Calculator:
    def __init__(self):
        self.name = input("ชื่อของคุณ? ")
        print("สวัสดี คุณ, "+self.name+"!")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


calculator = Calculator()
x = float(input("เลขตัวแรก: "))
y = float(input("ลขตัวสอง: "))
print("บวก: ", calculator.add(x, y))
print("ลบ: ", calculator.subtract(x, y))
print("คูณ: ", calculator.multiply(x, y))
print("หาร: ", calculator.divide(x, y))
