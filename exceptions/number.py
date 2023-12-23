def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print(f"x is not a integer")
            pass
        except NameError:
            print(f"x is not defined")
    

main()