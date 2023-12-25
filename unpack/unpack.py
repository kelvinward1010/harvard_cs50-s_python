
def unpack():
    def total(galleons=0, sickles=0, knuts=0):
        return (galleons * 17 + sickles) * 29 + knuts


    coins_1 = [100, 50, 25]
    print(total(*coins_1), "Knuts")

    coins_2 = {"galleons": 100, "sickles": 50, "knuts": 25}
    print(total(**coins_2), "Knuts")

    print(total(), "Knuts")
    
    
def f(*args, **kwargs):
    print(f"Positinal 1: {args}")
    print(f"Positinal 2: {kwargs}")
    
f(100,25,50, galleons = 100, sickles=50, knuts=25)



