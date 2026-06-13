def display_student(name, roll, branch, semester):
    print("\n===== Student Information =====")
    print("Name:", name)
    print("Roll No:", roll)
    print("Branch:", branch)
    print("Semester:", semester)

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

display_student(name, roll, branch, semester)