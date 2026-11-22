students = {}
n = int(input("Enter number of students: "))
for i in range(n):
name = input("\nEnter student name: ")
marks = float(input("Enter marks: "))
students [name] = marks
print("\n ===== STUDENT RESULTS ===== ")
for name, marks in students.items():
if marks >= 90:
grade = "A"
elif marks >= 80:
grade = "B"
elif marks >= 70:
grade = "C"
elif marks >= 60:
grade = "D"
elif marks >= 40:
grade = "E"
else:
grade = "F"
print("\nStudent Name: ", name)
print ("Marks:", marks)
print("Grade:", grade)
