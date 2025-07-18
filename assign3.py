import math

class Math:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Error: Division by zero"

    def power(self, base, exponent):
        return base ** exponent
    
    def sin(self, angle_deg):
        return math.sin(math.radians(angle_deg))

    def cos(self, angle_deg):
        return math.cos(math.radians(angle_deg))

    def tan(self, angle_deg):
        if angle_deg % 180 == 90:
            return "Error: tan undefined at 90°, 270°, ..."
        return math.tan(math.radians(angle_deg))
    
    def sqrt(self, x):
        if x >= 0:
            return math.sqrt(x)
        return "Error: Negative number"

    def factorial(self, n):
        if n < 0:
            return "Error: Negative number"
        return math.factorial(n)

    def modulus(self, a, b):
        return a % b

    def absolute(self, x):
        return abs(x)

    def log(self, x, base=10):
        if x > 0:
            return math.log(x, base)
        return "Error: Log of non-positive number"



calc = Math()

print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(10, 4))
print("Multiply:", calc.multiply(2, 3))
print("Divide:", calc.divide(10, 2))
print("Power:", calc.power(2, 4))
print("Sqrt:", calc.sqrt(16))
print("Factorial:", calc.factorial(5))
print("Modulus:", calc.modulus(10, 3))
print("Absolute:", calc.absolute(-7))
print("Log base 10:", calc.log(100))
print("sin(30°):", calc.sin(30))      # 0.5
print("cos(60°):", calc.cos(60))      # 0.5
print("tan(45°):", calc.tan(45))      # 1.0
print("tan(90°):", calc.tan(90))      # Error





# list as dictationary



dict_like = [("name", "Alice"), ("age", 25), ("city", "Delhi")]

def get_value(key):
    for k, v in dict_like:
        if k == key:
            return v
    return None  

def set_value(key, value):
    for i in range(len(dict_like)):
        if dict_like[i][0] == key:
            dict_like[i] = (key, value)
            return
    dict_like.append((key, value)) 

print(get_value("name"))   
set_value("age", 30)
set_value("country", "India")
print(dict_like)
