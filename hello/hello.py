name = input("What's your name?")
name = name.strip().title()

#Split the name into first name and last name

first, last = name.split(" ")

print(f"My name is: {name}")

print(f"First name is: {first}")
print(f"Last name is: {last}")