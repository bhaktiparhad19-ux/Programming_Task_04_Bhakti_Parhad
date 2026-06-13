from datetime import datetime

now = datetime.now()

file = open("activity_log.txt", "a")

file.write(
    f"{now} - Program Started\n"
)

file.close()

print("Log Created Successfully")