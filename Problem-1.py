class Claculator:
    def __init__(self, a: float, b: float, op: str):
        self.a = a
        self.b = b
        self.op = op.lower()
    
    def calculator(self):
        if self.op == "add":
            return self.a + self.b
        elif self.op == "subtract":
            return self.a - self.b
        elif self.op == "multiply":
            return self.a * self.b
        elif self.op == "divide":
            return self.a // self.b
        else:
            return "invalid operation"
        
if __name__ == "__main__":
    a = float(input("Entṇer first number (a) : "))
    b = float(input("Enter second numbeer (b) : "))
    op = input("Enter the operation (add, subtract, multiply, divide) : ")

    calc = Claculator(a, b, op)
    print("Result : ", calc.calculator())