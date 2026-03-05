
class Calculator:

    def sum(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def restar(self, a: int, b: int) -> int:
        return self.subtract(a, b)

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("no se puede dividir entre cero")
        return a / b