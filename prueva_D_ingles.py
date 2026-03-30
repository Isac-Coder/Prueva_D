import os, csv
from extras import *

Inventory = []

def Menu():
    print("SELECT AN OPTION")
    print("1. Register Student\n2. View Student\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")

def Register_Students():
    while True:
        Clear_screen()
        try:
            ID = input("Enter Student ID:\n# ")
            if not ID.isdigit():
                raise ValueError
            ID = int(ID)
            if ID <= 0:
                raise ValueError
        except ValueError:
            print(f"The ID {ID} is not valid")
            input("Press Enter to continue...")
            continue

        if any(s["ID"] == ID for s in Inventory):
            print(f"The ID {ID} is already registered")
            input("Press Enter to continue...")
            continue

        NAME = input("Enter Student Name:\n# ").strip().title()
        if not NAME or not all(c.isalpha() or c.isspace() for c in NAME):
            print("Invalid Name.")
            input("Press Enter to continue...")
            continue

        try:
            AGE = input("Enter Student Age:\n# ")
            if not AGE.isdigit():
                raise ValueError
            AGE = int(AGE)
            if AGE <= 0:
                raise ValueError
        except ValueError:
            print("Invalid Age.")
            input("Press Enter to continue...")
            continue

        COURSE = input("Enter Course or Program Name:\n# ").strip().title()
        
        try:
            STATUS = input("Enter Status (1. Active / 2. Inactive):\n# ")
            if STATUS in ["1", "Active"]:
                STATUS = "Active"
            elif STATUS in ["2", "Inactive"]:
                STATUS = "Inactive"
            else:
                raise ValueError
        except ValueError:
            print("Invalid Status.")
            input("Press Enter to continue...")
            continue
        
        Student = {
            "ID": ID,
            "Name": NAME,
            "Age": AGE,
            "COURSE": COURSE,
            "STATUS": STATUS
        }
        
        Inventory.append(Student)
        print(f"Student {NAME} registered successfully.")
        
        choice = input("Do you want to register another student? (yes/no): ").lower()
        if choice == "no":
            break

def View_Student():
    if not Inventory:
        print("No students in the database.")
        input("Press Enter to continue...")
        return

    try:
        ID = input("Enter the Student ID to view:\n# ")
        if not ID.isdigit():
            raise ValueError
        ID = int(ID)
    except ValueError:
        print("Invalid ID.")
        input("Press Enter to continue...")
        return
    
    for Student in Inventory:
        if Student["ID"] == ID:
            print(f"ID: {Student['ID']}\nName: {Student['Name']}\nAge: {Student['Age']}\nCourse: {Student['COURSE']}\nStatus: {Student['STATUS']}")
            break
    else:
        print(f"No student found with ID {ID}")
    input("Press Enter to continue...")

def Search_Student():
    if not Inventory:
        print("No students in the database.")
        input("Press Enter to continue...")
        return

    search_term = input("Enter ID or Name to search:\n# ").strip().title()
    found = False

    for student in Inventory:
        if str(student["ID"]) == search_term or student["Name"] == search_term:
            print("-" * 20)
            print(f"ID: {student['ID']}\nName: {student['Name']}\nCourse: {student['COURSE']}\nStatus: {student['STATUS']}")
            print("-" * 20)
            found = True
            break

    if not found:
        print(f"No match found for: {search_term}")
    input("Press Enter to continue...")

def Update_Student():
    if not Inventory:
        print("No students in the database.")
        input("Press Enter to continue...")
        return

    try:
        ID = int(input("Enter Student ID to update:\n# "))
    except ValueError:
        print("Invalid ID.")
        return
    
    student_to_update = next((s for s in Inventory if s["ID"] == ID), None)

    if not student_to_update:
        print("Student not found.")
        input("Press Enter to continue...")
        return

    print(f"Current Course: {student_to_update['COURSE']}")
    new_course = input("Enter new course (leave blank to keep current):\n# ").strip().title()
    if new_course:
        student_to_update["COURSE"] = new_course

    print(f"Current Status: {student_to_update['STATUS']}")
    new_status = input("Enter new status (1. Active, 2. Inactive, blank to keep):\n# ")
    if new_status == "1":
        student_to_update["STATUS"] = "Active"
    elif new_status == "2":
        student_to_update["STATUS"] = "Inactive"

    print("Student updated successfully.")
    input("Press Enter to continue...")

def Delete_Student():
    if not Inventory:
        print("No students in the database.")
        input("Press Enter to continue...")
        return

    try:
        ID = int(input("Enter Student ID to delete:\n# "))
    except ValueError:
        print("Invalid ID.")
        return
    
    for student in Inventory:
        if student["ID"] == ID:
            Inventory.remove(student)
            print("Student deleted successfully.")
            break
    else:
        print("Student not found.")
    input("Press Enter to continue...")
