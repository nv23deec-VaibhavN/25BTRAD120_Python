students = []

def add_student():
    name = input("Enter student name: ")
    students.append({"name": name, "attendance": []})
    print("Student added successfully!")

def mark_attendance():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            status = input("Enter status (P/A): ").upper()
            if status == "P":
                student["attendance"].append("Present")
            elif status == "A":
                student["attendance"].append("Absent")
            else:
                print("Invalid status!")
                return
            print("Attendance recorded!")
            return
    print("Student not found!")

def update_attendance():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            if not student["attendance"]:
                print("No attendance records!")
                return
            print("Records:", student["attendance"])
            record = int(input("Record number to update: "))
            if 1 <= record <= len(student["attendance"]):
                status = input("New status (P/A): ").upper()
                if status == "P":
                    student["attendance"][record-1] = "Present"
                elif status == "A":
                    student["attendance"][record-1] = "Absent"
                else:
                    print("Invalid status!")
                    return
                print("Attendance updated!")
            else:
                print("Invalid record number!")
            return
    print("Student not found!")

def display_attendance():
    for student in students:
        print(student["name"], ":", student["attendance"])

def attendance_report():
    threshold = float(input("Enter attendance threshold (%): "))
    for student in students:
        total = len(student["attendance"])
        present = student["attendance"].count("Present")
        percentage = present / total * 100 if total else 0
        print(student["name"], ":", round(percentage, 2), "%")
        if percentage < threshold:
            print("Below attendance threshold")

while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Update Attendance")
    print("4. Display Attendance")
    print("5. Attendance Percentage")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        update_attendance()
    elif choice == "4":
        display_attendance()
    elif choice == "5":
        attendance_report()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
