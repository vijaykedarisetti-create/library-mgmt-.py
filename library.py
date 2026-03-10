students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "marks": marks}

def display_students():
    for roll, info in students.items():
        print(roll, info["name"], info["marks"])

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted")

while True:
    print("\n1.Add Student\n2.Display Students\n3.Delete Student\n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
