import sys
import argparse

#mypy namefile.py

class Cat:
    MEOWS = 3
    
    def moew(self):
        for _ in range(Cat.MEOWS):
            print("moew")
               
cat = Cat()


def meomeo_a():
    def moew(n: int) -> str:
        return "moewn\n" * n
        # for _ in range(n):
        #     print("moew")
            
    number = int(input("Number: "))
    moews: str = moew(number)
    print(moews, end="")


def meomeo():
    if len(sys.argv) == 1:
        print("meomeo")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for _ in range(n):
            print("meomeo")
    else:
        print("usege: meow.py")
        
        
def meow_3():
    parser = argparse.ArgumentParser(description="Meo like cat!")
    parser.add_argument("-n", default=1, help="number of items to meow", type=int)
    args = parser.parse_args()
    
    for _ in range(int(args.n)):
        print("meow")