#Task 17 :  Convert Celsius to Fahrenheit and display the result using an f-string with two decimal places.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
