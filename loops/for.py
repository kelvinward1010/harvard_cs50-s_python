def funcList():
    for i in [0,1,2]:
        print("Meow")

def funcRange():
    for i in range(0,3):
        print("Meow")
        
    for i in range(3):
        print("Meow")
    

def funcList():
    students = ["Hermione", "Harry", "Ron"]

    for i in range(len(students)):
        print(f"{i + 1}.",students[i])
        
def funcDictionary():
    houses = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Stytherin",
    }
    
    for i in houses:
        print(f"{i} : {houses[i]}", i, sep=", ")


def funcListCoverDict():
    students = [
        {
            "name": "Hermione",
            "house": "Gryffindor",
            "patronus": "Otter",
        },
        {
            "name": "Harry",
            "house": "Gryffindor",
            "patronus": "Stag",
        },
        {
            "name": "Ron",
            "house": "Gryffindor",
            "patronus": "Jasck Russell terrier",
        },
        {
            "name": "Draco",
            "house": "Stytherin",
            "patronus": None,
        },
    ]
    
    for i in students:
        print(f"{i["name"]} - {i["house"]} - {i["patronus"]}")
    
    #Another way
    print("\nAnother way\n")
    for i in range(len(students)):
        print(f"{i+1}. {students[i]["name"]} - {students[i]["house"]} - {students[i]["patronus"]}")
        
funcListCoverDict()