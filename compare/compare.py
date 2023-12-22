x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print(f"Result: x({x}) < y({y})")
elif x > y:
    print(f"Result: x({x}) > y({y})")
elif x == y:
    print(f"Result: x({x}) = y({y})")