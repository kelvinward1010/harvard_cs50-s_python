students = [
    {"name": "Hermione", "house": "Gryyffindor"},
    {"name": "Harry", "house": "Gryyffindor"},
    {"name": "Ron", "house": "Gryyffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

def main__gryffindors_1():
    gryffindors = [
        students["name"] for students in students if students["house"] == "Gryyffindor"
    ]

    for gryffindor in gryffindors:
        print(gryffindor)
    

def main__gryffindors_2():
    def is_gryffindor(s):
        return s["house"] == "Gryyffindor"

    gryffindors = filter(is_gryffindor, students)
    
    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor)
        
def main__gryffindors_3():

    gryffindors = filter(lambda s: s["house"] == "Gryyffindor", students)
    
    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor)
        


def main__gryffindors_4():
    students_2 = ["Hermione", "Harry", "Ron"]

    gryffindors_2 = []

    for student in students_2:
        gryffindors_2.append({"name": student, "house": "Gryyffindor"})
        
    print(gryffindors_2)
    
    

def main__gryffindors_5():
    students_2 = ["Hermione", "Harry", "Ron"]

    gryffindors_2 = [{"name": student, "house": "Gryyffindor"} for student in students_2 if student == "Hermione" ]
        
    print(gryffindors_2)
    

def main__gryffindors_6():
    students_2 = ["Hermione", "Harry", "Ron"]

    gryffindors_2 = {student: "Gryyffindor" for student in students_2}
        
    print(gryffindors_2)


def main__gryffindors_7():
    students_2 = ["Hermione", "Harry", "Ron"]

    for i in range(len(students_2)):
        print(i + 1, students_2[i])
    
def main__gryffindors_8():
    students_2 = ["Hermione", "Harry", "Ron"]

    for i, student in enumerate(students_2):
        print(i + 1, student)
    
main__gryffindors_8()
