#print("meow\n" * 3, end="")

#fisrt
def meow_fisrt():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break

    for _ in range(n):
        print("Meow", _)
        

#second
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()