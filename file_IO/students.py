def read_file():
    with open("students.csv") as file:
        for line in file:
            # row = line.rstrip().split(',')
            # print(f"| {row[0]} | {row[1]} |")
            
            name, house = line.rstrip().split(',')
            print(f"| {name} | {house} |")


def read_file_other_ways():
    students = []
    
    with open("students.csv") as file:
        for line in file:
            
            name, house = line.rstrip().split(',')
            students.append(f"| {name} | {house} |")
    for student in sorted(students):
        print(student)
        
read_file_other_ways()
    
    