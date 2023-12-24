

#mypy namefile.py

class Cat:
    MEOWS = 3
    
    def moew(self):
        for _ in range(Cat.MEOWS):
            print("moew")
               
cat = Cat()


def moew(n: int) -> str:
    return "moewn\n" * n
    # for _ in range(n):
    #     print("moew")
            
number = int(input("Number: "))
moews: str = moew(number)
print(moews, end="")