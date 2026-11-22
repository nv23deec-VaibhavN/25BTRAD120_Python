# Simple Bill Generator
print("--- Store Checkout ---")
#1. Get Input
item = input("What are you buying? ")
price = float(input("How much does one cost? "))
quantity = float(input("How many are you buying? "))
#2. Do the Math
subtotal = price * quantity
tax = subtotal * 0.05 # 5% tax
grand_total = subtotal + tax
#3. Print the Receipt
print("\n--- Your Receipt ---")
print("Item: ", item)
print("Quantity: "
, quantity)
print("Subtotal: $"
, subtotal)
print("Tax: $", tax)
print("Total Pay: $", grand_total)
print("--------------------")
