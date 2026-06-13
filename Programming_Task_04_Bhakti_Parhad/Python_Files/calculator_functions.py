def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "5":
        print("Program Closed")
        break

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result:", addition(num1, num2))

    elif choice == "2":
        print("Result:", subtraction(num1, num2))

    elif choice == "3":
        print("Result:", multiplication(num1, num2))

    elif choice == "4":
        print("Result:", division(num1, num2))

    else:
        print("Invalid Choice")