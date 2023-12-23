def funcNames():
    names = []

    for _ in range(3):
        name = input("What's your name? ")
        names.append(name)
        
    for name in sorted(names):
        print(f"hello, {name}")
        
    
def write_file():
    name = input("What's your name? ")
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")
        file.close()

def read_file():
    with open("names.txt", "r") as file_reader:
        for line in file_reader:
            print(f"Hello {line.rstrip()}")
        #lines = file_reader.readlines()
    
    # for line in lines:
    #     print(f"Hello {line.rstrip()}", end=", ")

def append_line():
    names = []
    with open("names.txt") as file_reader:
        for line in file_reader:
            names.append(line.rstrip())
    
    print(f"Data: {names}")
    for name in sorted(names, reverse=True):
        print(f"Hello, {name}")
        

if __name__ == "__main__":
    append_line()