name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
marks = input("Enter Marks: ")

file = open("student_data.txt", "w")

file.write(f"Name: {name}\n")
file.write(f"Roll No: {roll}\n")
file.write(f"Branch: {branch}\n")
file.write(f"Marks: {marks}\n")

file.close()

print("\nStudent Record Saved Successfully")

print("\nReading File...\n")

file = open("student_data.txt", "r")

print(file.read())

file.close()