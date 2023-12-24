class Wizard:
    def __init__(self, name="Albus"):
        if not name:
            raise ValueError("Missing name!")
        self.name = name

class Student(Wizard):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
        
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
wizard = Wizard()
student = Student("Harruy", 3.5)
professor = Professor("Kelvin", "Developer")


print(wizard.name)
print(student.name, student.gpa)
print(professor.name, professor.subject)