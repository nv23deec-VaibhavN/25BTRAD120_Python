import csv
from pathlib import Path
FILE = Path("students. csv")
FIELDS = ["Roll No", "Name", "Marks"]
def load_records():
if not FILE.exists() :
return []
with FILE. open("r",open("r", newline="", encoding="utf-8") as f:
return list(csv.DictReader(f))
def save_records (records ) :
with FILE.open("w", newline="", encoding="utf-8") as f:
writer = csv.DictWriter(f, fieldnames=FIELDS)
writer.writeheader()
writer.writerows (records)
def add_student (roll, name, marks):
records = load_records()
if any(r["Roll No"] == roll for r in records):
print("Roll number already exists.")
return
if not name.strip() or not (0 <= marks <= 100)
print("Invalid student details.")
return
records. append ( {
"Roll No": roll,
Name": name,
Marks": str(marks)

})

save_records(records
print("Student record added successfully. ")
def display_students ():
records = load_records()
if not records:
print("No student records found.")
return
print("\nROLL NO  NAME  MARKS")

print (" -----------")

for r in records :
print(f' {r["Roll No"] :< 9} {r["Name"] :< 16} {r["Marks"]}'
def search_student(roll) :
for r in load_records():
if r["Roll No"] == roll:
print("Record found:", r
return
print("Student not found.")
def update_student(roll, new_marks):
records = load_records ()
for r in records :
if r["Roll No"] == roll:
if not (0 <= new_marks <= 100):
print("Marks must be between 0 and 100.")
return
r["Marks"] = str(new_marks)
save_records (records )
print("Student record updated successfully.")
return
print("Student not found.")
# Demonstration of all required file operations.
FILE. unlink(missing_ok=True) # Start with a clean sample file.
add_student("101", "Aarav", 85)
add_student("102", "Diya", 92)
display_students ()
search_student("102")
update_student("101", 90)
display_students()
