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
    
    #Getter
    @property
    def house(self):
        return self._house
    
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    #name, house = get_student()
    student_1 = get_student()
    
    # if student["name"] == "kelvin":
    #     student["house"] = "Gryphindor"
    #print(f"{student.name} from {student.house}")
    
    # student.call_info()
    # print(f"Expecto Patronum: {student.charm()}")
    #student.house = "My house"
    
    print(student_1)
    
    

def get_student():
    
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name=name, house=house, patronus=patronus)
    
    return student


class Student_2():
    def __init__(self, name, house, patronus="Something?"):
        if not name or not house:
            raise ValueError("Missing name or house!")
        self.name = name
        self.house = house
        self.patronus = patronus
        
    def __str__(self):
        return f"{self.name} from {self.house} in {self.patronus}"
    
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)


def main_2():
    student_1 = Student_2.get()
    print(student_1)



if __name__ == "__main__":
    main_2()