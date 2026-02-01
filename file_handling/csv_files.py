import csv

# Writing to a CSV file
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Alex", 20, "Python"])
    writer.writerow(["Sam", 22, "Data Science"])

print("CSV file written successfully")

# Reading from a CSV file
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
