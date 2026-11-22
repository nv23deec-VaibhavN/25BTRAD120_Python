# Prime number check
n = int(input("Enter a number: "))
if n <= 1:
 print("Not a prime number")
else:
 prime = True
 for i in range(2, n):
 if n % i == 0:
 prime = False
 break
 if prime:
 print("Prime number")
 else:
 print("Not a prime number")
# Factorial
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
 factorial *= i
print("Factorial =", factorial)
