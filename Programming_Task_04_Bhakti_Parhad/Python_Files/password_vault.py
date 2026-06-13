website = input("Enter Website Name: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

file = open("vault.txt", "a")

file.write(f"Website: {website}\n")
file.write(f"Username: {username}\n")
file.write(f"Password: {password}\n")
file.write("-------------------\n")

file.close()

print("\nRecord Saved Successfully")

print("\nSaved Records:\n")

file = open("vault.txt", "r")

print(file.read())

file.close()