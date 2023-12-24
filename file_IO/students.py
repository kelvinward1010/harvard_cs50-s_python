import csv

def write_csv():
    name = input("What's your name? ")
    house = input("What's your house? ")
    
    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"])
        writer.writerow({'name': "name", 'house': "house"})
        writer.writerow({'name': name, 'house': house})

write_csv()

def file_1():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(',')
            print(f"| {name} | {house} |")


def file_2():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            
            name, house = line.rstrip().split(',')
            students.append(f"| {name} | {house} |")
    for student in sorted(students):
        print(student)


def file_3():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(',')
            student = {
                "name": name,
                "house": house
            }
            students.append(student)
            
    
    for student in sorted(students, key=lambda student: student["name"], reverse=True):
        print(f"| {student["name"]} | {student["house"]} |")

def file_4():
    students = []
    
    with open("students.csv") as file:
        reader = csv.reader(file)
        for name, house in reader:
            student = {
                "name": name,
                "house": house
            }
            students.append(student)
            
    
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"| {student["name"]} | {student["house"]} |")
        

def file_5():
    students = []
    
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                "name": row["name"],
                "house": row["house"]
            }
            students.append(student)
            
    
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"| {student["name"]} | {student["house"]} |")
    
