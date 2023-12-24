students = [
    {"name": "Hermione", "house": "Gryyffindor"},
    {"name": "Harry", "house": "Gryyffindor"},
    {"name": "Ron", "house": "Gryyffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    # if student["house"] not in houses:
    #     houses.append(student["house"])
    
    houses.add(student["house"])
        
        
for house in sorted(houses):
    print(house)