import math
print("--- Simple Calculator ---")
print("Operations: +, -, *, /")
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if op == "+":
 print(f"Result: {a} + {b} = {a + b}")
elif op == "-":
 print(f"Result: {a} - {b} = {a - b}")
elif op == "*":
 print(f"Result: {a} * {b} = {a * b}")
elif op == "/" and b != 0:
 print(f"Result: {a} / {b} = {a / b}")
elif op == "/":
 print("Error: Cannot divide by zero!")
else:
 print("Invalid operator entered.")
print("--- Area Calculator ---")
print("\nRectangle:")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
print(f"The area of the rectangle is: {length * width}")
print("\nCircle:")
radius = float(input("Enter the radius: "))
print(f"The area of the circle is: {round(math.pi * radius ** 2, 2)}")
