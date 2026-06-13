def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


marks = []

for i in range(1, 6):
    mark = float(input(f"Enter Marks of Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

grade = calculate_grade(percentage)

print("\n===== Result =====")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)