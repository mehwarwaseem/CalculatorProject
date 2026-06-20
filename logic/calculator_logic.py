class CalculatorLogic:
    def __init__(self, db):
        self.db = db

    def calculate(self, a, b, op):

        if op == "+":
            result = a + b

        elif op == "-":
            result = a - b

        elif op == "*":
            result = a * b

        elif op == "/":
            if b == 0:
                result = "Error: Cannot divide by zero"
            else:
                result = a / b

        elif op == "%":
            if b == 0:
                result = "Error: Cannot modulo by zero"
            else:
                result = a % b

        elif op == "^":
            result = a ** b

        else:
            result = "Invalid Operation"

        self.db.save(f"{a} {op} {b}", result)
        return result