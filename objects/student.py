class Student():
    def __init__(self, name, house, patronus="Something?"):
        if not name or not house:
            raise ValueError("Missing name or house!")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house} in {self.patronus}"
    
    def call_info(self):
        print(f"Calling {self.name} from {self.house}")
        
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Stag"
            case "Otter":
                return "Otter"
            case _:
                return "/"

def main():
    #name, house = get_student()
    student = get_student()
    
    # if student["name"] == "kelvin":
    #     student["house"] = "Gryphindor"
    #print(f"{student.name} from {student.house}")
    
    student.call_info()
    print(f"Expecto Patronum: {student.charm()}")
    print(student)
    

def get_student():
    
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name=name, house=house, patronus=patronus)
    
    return student


if __name__ == "__main__":
    main()