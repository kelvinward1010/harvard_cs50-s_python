def main():
    x = int(input("What's x?  "))

    if is_event(x):
        print("Even")
    else:
        print("Odd")
        
def is_event(n):
    return True if n % 2 == 0 else False

main()