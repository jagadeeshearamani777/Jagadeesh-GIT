class Calculator:

    def __init__(self,a=0,b=20) -> None:
        self.a=a
        self.b=b

    def addition(self) -> int:
        return self.a+self.b

    def subtraction(self) -> float:
        return self.a-self.b

    def Multiplication(self) -> float:
        return self.a*self.b
    

cal=Calculator(a=3,b=4)
print(f"Adding the values:-  {cal.addition()}")
