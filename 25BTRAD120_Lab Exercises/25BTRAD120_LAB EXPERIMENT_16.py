import random
def roll_dice(number_of_rolls):
if number_of_rolls <= 0:
print("Please enter a positive number of rolls.")
return
frequency = {number: 0 for number in range(1, 7)}
print("DICE ROLL RESULTS")
print("-----------------------")
for roll in range(1, number_of_rolls + 1) :
result = random.randint(1, 6)
frequency [result] += 1
print(f"Roll {roll}: {result}")
print("\nFREQUENCY OF EACH NUMBER")
print("------------------------")
for number, count in frequency.items():
print(f"{number} : {count}")
# Seed is used here so the sample output is reproducible.
random. seed (7)
roll_dice(10)
