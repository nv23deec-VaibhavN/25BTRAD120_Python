import random
# Generate a 6-digit OTP
otp = random.randint(100000, 999999)
print("Your OTP is:", otp)
# Accept OTP from the user
entered_otp = int(input("Enter the OTP: "))
# Verify OTP
if entered_otp == otp:
 print("OTP verified successfully.")
  else:
 print("Invalid OTP.")
