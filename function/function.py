def main():
    name = input("What's your name? ")
    hello(name)

def hello(name="World!"):
    age = int(input("How old are you? "))
    name = name.strip().title()
    
    print(f"Hello: {name}, you have: {age} years old")


main()