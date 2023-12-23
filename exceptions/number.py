def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print(f"x is not a integer")
        except NameError:
            print(f"x is not defined")

    return x

main()